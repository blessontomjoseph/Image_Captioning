from transformers import ViTImageProcessor, AutoTokenizer
import torch

feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

torch.save(feature_extractor,'feature_extractor')
torch.save(tokenizer,"tokenizer")