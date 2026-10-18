#!/usr/bin/env python3
"""
This script defines a Dataset class for loading and preparing
a dataset for machine translation from Portuguese to English.
"""
import transformers
from setup import load_pt2en


class Dataset:
    """
    This class loads and preprocess a dataset for machine translation.
    """
    def __init__(self):
        """
        This method initializes the Dataset class by loading the train and
        validation splits and creating tokenizers for Portuguese and English.
        """
        # Load dataset splits
        self.data_train, self.data_valid = load_pt2en()

        # Create tokenizers
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
        """
        This method creates sub-word tokenizers for the dataset using
        pre-trained models.
        Args:
            data: tf.data.Dataset containing tuples (pt, en),
                  where `pt` is a Portuguese sentence and `en` is the
                  corresponding English sentence.
        Returns:
            tokenizer_pt: Portuguese tokenizer.
            tokenizer_en: English tokenizer.
        """
        # Prepare a list of Portuguese and English sentences
        pt_sentences = []
        en_sentences = []
        
        # Iterate over the dataset to gather sentences
        for pt, en in data:
            pt_sentences.append(pt.numpy().decode('utf-8'))
            en_sentences.append(en.numpy().decode('utf-8'))

        # Create tokenizers for Portuguese and English
        tokenizer_pt = transformers.AutoTokenizer.from_pretrained(
            'neuralmind/bert-base-portuguese-cased', use_fast=True,
            clean_up_tokenization_spaces=True)
        tokenizer_en = transformers.AutoTokenizer.from_pretrained(
            'bert-base-uncased', use_fast=True,
            clean_up_tokenization_spaces=True)

        # Train the tokenizers
        tokenizer_pt = tokenizer_pt.train_new_from_iterator(pt_sentences,
                                                            vocab_size=2**13)
        tokenizer_en = tokenizer_en.train_new_from_iterator(en_sentences,
                                                            vocab_size=2**13)

        # Return the tokenizers
        return tokenizer_pt, tokenizer_en


if __name__ == '__main__':
    # Initialize the dataset
    dataset = Dataset()
    
    # Print the validation sentences to match the expected stdout format
    for pt, en in dataset.data_valid.take(5):
        print(pt.numpy().decode('utf-8'))
        print(en.numpy().decode('utf-8'))
