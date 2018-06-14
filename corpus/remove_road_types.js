const fs = require('fs');
const path = require('path');
const lines = fs.readFileSync(path.join(__dirname, './streets.txt'), 'utf-8').split(/\r?\n/);

const roadTypes = buildRoadTypesMap();

/**
 * @returns Map<string, number> mapping road type to its frequency count
 */
function buildRoadTypesMap() {
    const map = new Map();
    lines.forEach(l => {
        const words = l.split(/\s+/);
        if (words.length === 1) {
            return;
        }

        const first = words[0];
        const last = words[words.length - 1];

        // Prevent shit like "San Carmeloway", "Via Italia"
        if (/San|Via/.test(first)) {
            return;
        }

        if (last.length === 0 ||/\d/.test(last) || /north|south|east|west/i.test(last)) {
            return;
        }

        const count = map.get(last) || 0;
        map.set(last, count + 1);
    });
    return map;
}

/**
 * Chucks roadTypes into an array of CSV entries, sorted by most to least frequent.
 * @return string[]
 */
function dumpRoadTypes(roadTypes) {
    return Array.from(roadTypes)
        .sort((entry1, entry2) => entry2[1] - entry1[1]) // sort by frequency
        .map(entry => `${entry[0]},${entry[1]}`); // join into csv
}

const withoutRoadType = lines.map(line => {
    const segments = line.split(/\s/);

    // remove street type suffix
    if (roadTypes.has(segments[segments.length - 1])) {
        segments.splice(segments.length - 1, 1);
    }
    return segments.join(' ');
}).filter(s => s.length).sort();

fs.writeFileSync(path.join(__dirname, './streets_no_roadtype.txt'), withoutRoadType.join('\n'));
fs.writeFileSync(path.join(__dirname, './roadtypes.txt'), dumpRoadTypes(roadTypes).join('\n'));