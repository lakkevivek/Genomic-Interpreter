# #Output-Genomic Model output image,original image,white extraction image
from swin1d.module import swin_1d_block
from swin1d.examples import (
    random_text_generator,
    generate_random_dna,
    onehot_encoder,
)

import torch
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

import random
torch.manual_seed(42)
random.seed(42)
np.random.seed(42)

'''takes a DNA sequence as input and visualizes it using a color mapping. The DNA bases ('A', 'T', 'C', 'G') are mapped
to numeric values, and the sequence is displayed as an image using matplotlib.pyplot.'''

def visualize_dna_sequence(sequence):
    # Check if the input sequence is a list of strings
    if isinstance(sequence, list):
        # Concatenate the list of strings into a single string
        sequence = ''.join(sequence)

    # Define a mapping of DNA bases to color intensity values
    mapping = {'A': 0.8, 'T': 0.5, 'C': 1, 'G': 1.5}

    # Create an array of color intensity values based on the DNA sequence
    colors = np.array([mapping[base] for base in sequence])

    # Reshape the color array to have a single row and as many columns as bases in the sequence
    colors_reshaped = colors.reshape(1, -1)

    # Display the color array as an image using matplotlib
    plt.imshow(colors_reshaped, cmap='coolwarm', aspect=100)

    # Remove x and y axis ticks
    plt.xticks([])
    plt.yticks([])

    # Set the title of the plot
    plt.title("DNA Sequence")

    # Show the plot
    plt.show()

    
    
''' takes an image array and a threshold as input. It performs thresholding on the input image array 
to extract the white part, returning a binary array where white pixels are represented by 1.0.'''
def extract_white_part(image_array, threshold=0.5):
    # Thresholding to extract white part

    # Using NumPy, compare each pixel value in the image_array to the threshold
    # The comparison results in a boolean array where True corresponds to pixels greater than the threshold
    thresholded_array = (image_array > threshold)

    # Convert the boolean array to a binary array by using the astype(float) method
    # Now, True becomes 1.0 and False becomes 0.0
    white_part = thresholded_array.astype(float)

    # Return the binary array representing the white part after thresholding
    return white_part

#####

# def test_genomic_model(seq_length=512):
#     # input_sequence = generate_random_dna(seq_length)
#     input_sequence = ['CAAATGCCTAAACCCGATCTGAATCGTGTTTTACTGTTATCACGCGTGAAAACTGTCTAGCGCAGTGGGATCTTATGCAAGTTATAGGTCCCATTCTGGCGCGCCTCTTGCTGTGCAACTTGCGTGAGGAGGGGTCTTTTAACCTCTTAACACTTACTAGAGACAAAAACTGAACGTACTCAGGGTTCTTCCCGAGGTTTATCTTCTGCGTTAGCAAACCTGAGTCTGCGTTGACCCTCGATTTTTAAGCCGTATAGAAGACGGTGTAGTGGGTGGTTCGTCTTTGCTGAAACGAGACCGCGTAGTACAGGGGCTGTATGACTGGGGACCTCTGAAAATCCAATACTGAGTAGAAACAAGCACTCCTGCTCCCACTACGTTCAACCACCTAATCGTGATCGAGATAAAAGATTATGGGCCACCGATAAGTCGATTTTCTGACATTGTGTATACGTGCAGTAGGATTATATTCTGGCATGGAAAAACCTGTCTTTAGGGTGCAAGGTATAACA']
#     print("Generated DNA Sequence:", input_sequence)  # Print the generated sequence
#     encode_input = onehot_encoder(input_sequence)
#     model = swin1d_block(4)
#     output = model(encode_input)
#     print(output.shape)

#     # Convert torch tensor to NumPy array
#     output_array = output.detach().numpy().squeeze()
    
#     # Visualize the DNA sequence
#     visualize_dna_sequence(input_sequence)

#     # Convert NumPy array to PIL Image
#     image_data = visualize_genomic_model(output_array)
    
#     return image_data

# def visualize_genomic_model(output_array):
    
#     # Display the genomic model output
#     plt.subplot(1, 2, 1)
#     plt.imshow(output_array, cmap='gray')
#     plt.title("Genomic Model Output")
#     # Extract the white part
#     white_part = extract_white_part(output_array)

#     # Display the original image
#     # plt.subplot(1, 3, 2)
#     # plt.imshow(output_array, cmap='gray')
#     # plt.title("Original Image")

#     # Display the extracted white part
#     plt.subplot(1, 2, 2)
#     plt.imshow(white_part, cmap='gray')
#     plt.title("White Part")
#     # plt.axis('off')
#     image_buffer = BytesIO()
#     plt.savefig(image_buffer, format='png')
#     image_data = image_buffer.getvalue()
#     plt.close()
#     return image_data

#####
#####

'''generates a DNA sequence, prints it, encodes it using a one-hot encoder, 
and passes it through a Swin Transformer model (swin1d_block). The output shape of the model is printed.'''
def test_genomic_model(seq_length=512):
    input_sequence=['CAAATGCCTAAACCCGATCTGAATCGTGTTTTACTGTTATCACGCGTGAAAACTGTCTAGCGCAGTGGGATCTTATGCAAGTTATAGGTCCCATTCTGGCGCGCCTCTTGCTGTGCAACTTGCGTGAGGAGGGGTCTTTTAACCTCTTAACACTTACTAGAGACAAAAACTGAACGTACTCAGGGTTCTTCCCGAGGTTTATCTTCTGCGTTAGCAAACCTGAGTCTGCGTTGACCCTCGATTTTTAAGCCGTATAGAAGACGGTGTAGTGGGTGGTTCGTCTTTGCTGAAACGAGACCGCGTAGTACAGGGGCTGTATGACTGGGGACCTCTGAAAATCCAATACTGAGTAGAAACAAGCACTCCTGCTCCCACTACGTTCAACCACCTAATCGTGATCGAGATAAAAGATTATGGGCCACCGATAAGTCGATTTTCTGACATTGTGTATACGTGCAGTAGGATTATATTCTGGCATGGAAAAACCTGTCTTTAGGGTGCAAGGTATAACA']
    # input_sequence = generate_random_dna(seq_length)
    # input_sequence = [getUserInput()]
    print("Input DNA Sequence:", input_sequence)  # Print the sequence

    # Visualize the DNA sequence
    visualize_dna_sequence(input_sequence)

    encode_input = onehot_encoder(input_sequence)
    model = swin1d_block(4)
    output = model(encode_input)
    '''A tensor in PyTorch is a multi-dimensional array, similar to NumPy arrays.
      Tensors are the fundamental data structures in PyTorch, and they are used to represent 
      input data, parameters, and outputs in neural network models.'''
    print("Model Output Shape:", output.shape)

    '''Converts the model output tensor to a NumPy array, visualizes the genomic model output, 
    and displays the original image and the extracted white part using matplotlib.pyplot.'''
    # print(output)
    # Convert torch tensor to NumPy array
    output_array = output.detach().numpy().squeeze()

    # Display the genomic model output
    plt.subplot(1, 2, 1)
    plt.imshow(output_array, cmap='gray')
    plt.title("Genomic Model Output")

    # Extract the white part
    white_part = extract_white_part(output_array)

    # Display the extracted white part
    plt.subplot(1, 2, 2)
    plt.imshow(white_part, cmap='gray')
    plt.title("White Part")

    plt.show()


#####

'''creates a Swin Transformer model with specified parameters, such as the dimension and window size.'''
def swin1d_block(dim):
    window_size = 32
    stages = [
        (4, True, window_size),
        (2, False, window_size),
        (2, False, window_size),
        (2, False, window_size),
    ]
    model = swin_1d_block(stages, dim)
    return model

if __name__ == "__main__":
    # Generate the genomic model output and visualize
    test_genomic_model()