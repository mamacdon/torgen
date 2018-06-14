from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('corpus/streets.txt', num_epochs=3)
textgen.save(weights_path='textgenrnn_weights.hdf5')
