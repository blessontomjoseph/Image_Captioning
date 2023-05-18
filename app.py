import streamlit as st
import torch
from PIL import Image
import time
from transformers import VisionEncoderDecoderModel

feature_extractor=torch.load("feature_extractor")
tokenizer=torch.load("tokenizer")
device='gpu' if torch.cuda.is_available() else "cpu"

def predict_step(image,gen_kwargs):
    images = []
    in_image = Image.open(image)
    if in_image.mode != "RGB":
        in_image = in_image.convert(mode="RGB")
    images.append(in_image)
    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    caption = [pred.strip() for pred in preds]
    return caption[0]

max_new_tokens=[10,15,20,25,30]
min_new_tokens=[5,10,15,20,25]
num_beams=[2,5,10,15,20]
leangth_penalty=[0.2,0.8,1,1.2,1.8]
temperature=[0.2,0.5,1,1.5,2]
top_p=[1,0.95,0.9,0.85,0.7]
top_k=[0,500,300,200,100]

if __name__ == '__main__':
    st.sidebar.title("Customize your generated text!")
    descriptiveness = st.sidebar.slider("Descriptiveness", min_value=1, max_value=5, step=1,value=1)
    creativity = st.sidebar.slider("Creativity", min_value=1, max_value=5, step=1,value=1)
    factualness = st.sidebar.slider("Factualness", min_value=1, max_value=5, step=1,value=1)    
    
    gen_kwargs = {
            "max_new_tokens":max_new_tokens[descriptiveness-1],
            "min_new_tokens":min_new_tokens[descriptiveness-1],
            "num_beams":num_beams[creativity-1],  #diversity of text directly prop
            "temperature":float(temperature[creativity-1]),#randomness of the output /could be less factual
            "do_sample":factualness>1,  # below 3 makes it more deterministic 
            "top_k":top_k[factualness-1],
            "no_repeat_ngram_size":2,
              }
                  
    image=st.file_uploader('upload image')
    st.image(image)

    apply = st.sidebar.button('generate caption')

    if apply:
        with st.spinner("getting model from 🤗..."):
            model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        st.success('model ready!')
        with st.spinner("generating caption..."):
            start_time = time.time()
            caption=predict_step(image,gen_kwargs)
            response_time = time.time() - start_time
            
        st.success(f"""Success!~Elapsed Time: {response_time:.2f} seconds""")
        st.subheader("Generated Text:")
        st.text_area(" ", caption, height=100, key="generated_text")