## Image Captioning

In this demonstration, we utilize a pretrained model from Hugging Face, specifically the [model](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning), to generate captions from images.

The purpose of this showcase is to showcase how decoding parameters can be adjusted to achieve desired generation outcomes.

By introducing three newly created parameters, the decoding process can be controlled and the diversity of the generated output can be enhanced. These parameters are:

1. Descriptiveness: This parameter is influenced by the values assigned to max_new_tokens and min_new_tokens.

2. Creativity: The values of num_beams and temperature determine the level of creativity in the generated captions.

3. Factualness: The do_sample and top_p values contribute to controlling the factualness of the generated captions.

each of which are scaled from 1-5 to control its intensity

While it is important to note that the captions produced by these modified parameters may not always accurately convey the intended word meaning, still they provide an interesting representation for diversifying the generated text without requiring a complete understanding of the original parameters.

try it here 👉 [**WebApp**](https://blessontomjoseph-image-captioning-app-ydv7q4.streamlit.app/)
(the app is on freetier it  could run out of memory on multiple tries and crash) so,

try this in local, clone the repository and the use the below code to create a docker image and run it
```
docker build -t <image_name> .
docker run <image_name>
```
