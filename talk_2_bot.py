from test_dependencies import *



print('Chatting Bot Models built and ready to go!')

# Set dropout layers to eval mode
encoder.eval()
decoder.eval()

# Initialize search module
searcher = GreedySearchDecoder(encoder, decoder)
print("Start Chatting with the bot:*-----------------")
print("-" * 40)
print("*" * 40)
evaluateInput(encoder, decoder, searcher, voc)
