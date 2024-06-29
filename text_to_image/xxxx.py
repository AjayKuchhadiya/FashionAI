# Machine Learning libraries 
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from autho_token import auth_token


# Download stable diffusion model from hugging face 
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
stable_diffusion_model.to(device) 



# Generate image from text 
def generate_image(): 
    """ This function generate image from a text with stable diffusion"""
    with autocast(device): 
        image = stable_diffusion_model(prompt.get(),guidance_scale=8.5)["sample"][0]
    
    # Save the generated image
    image.save('generatedimage.png')
    
    # Display the generated image on the user interface
    img = ImageTk.PhotoImage(image)
    img_placeholder.configure(image=img) 