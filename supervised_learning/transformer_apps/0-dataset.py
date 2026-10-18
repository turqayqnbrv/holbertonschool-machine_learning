#!/usr/bin/env python3
"""Dataset class that loads and preps a dataset for machine translation"""
import transformers
from setup import load_pt2en


class Dataset:
    """Loads and preps the ted_hrlr_translate/pt_to_en dataset"""

    def __init__(self):
        """Class constructor"""
        self.data_train = load_pt2en('train')
        self.data_valid = load_pt2en('validation')
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
        """Creates sub-word tokenizers for the dataset

        data: tf.data.Dataset of (pt, en) tf.Tensor sentence pairs

        Returns: tokenizer_pt, tokenizer_en
        """
        pt_sentences = []
        en_sentences = []
        for pt, en in data:
            pt_sentences.append(pt.numpy().decode('utf-8'))
            en_sentences.append(en.numpy().decode('utf-8'))

        pt_base = transformers.AutoTokenizer.from_pretrained(
            'neuralmind/bert-base-portuguese-cased', use_fast=True)
        en_base = transformers.AutoTokenizer.from_pretrained(
            'bert-base-uncased', use_fast=True)

        tokenizer_pt = pt_base.train_new_from_iterator(
            pt_sentences, vocab_size=2**13)
        tokenizer_en = en_base.train_new_from_iterator(
            en_sentences, vocab_size=2**13)

        return tokenizer_pt, tokenizer_en
