import torch
import numpy as np
import torchvision.transforms as transforms
from torch.autograd import Variable
from network.Transformer import Transformer
from huggingface_hub import hf_hub_download
from PIL import Image

# Constants
STYLE_SHINKAI = "Makoto Shinkai"
STYLE_HOSODA = "Mamoru Hosoda"
STYLE_MIYAZAKI = "Hayao Miyazaki"
STYLE_KON = "Satoshi Kon"
STYLE_CHOICE_LIST = [STYLE_SHINKAI, STYLE_HOSODA, STYLE_MIYAZAKI, STYLE_KON]

MODEL_REPO = {
    STYLE_SHINKAI: ("akiyamasho/AnimeBackgroundGAN-Shinkai", "shinkai_makoto.pth"),
    STYLE_HOSODA: ("akiyamasho/AnimeBackgroundGAN-Hosoda", "hosoda_mamoru.pth"),
    STYLE_MIYAZAKI: ("akiyamasho/AnimeBackgroundGAN-Miyazaki", "miyazaki_hayao.pth"),
    STYLE_KON: ("akiyamasho/AnimeBackgroundGAN-Kon", "kon_satoshi.pth"),
}

def load_model(style):
    repo_id, filename = MODEL_REPO[style]
    model_path = hf_hub_download(repo_id=repo_id, filename=filename)
    model = Transformer()
    model.load_state_dict(torch.load(model_path, map_location=torch.device("cuda" if torch.cuda.is_available() else "cpu")))
    model.eval()
    return model

def transform_image(image):
    image = image.convert("RGB")
    image = np.asarray(image)[:, :, [2, 1, 0]]  # Convert RGB to BGR
    image = transforms.ToTensor()(image).unsqueeze(0)
    return -1 + 2 * image  # Normalize to (-1, 1)

def apply_style(image_path, style):
    image = Image.open(image_path)
    model = load_model(style)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    input_tensor = transform_image(image).to(device)
    with torch.no_grad():
        output_tensor = model(Variable(input_tensor))[0]
    output_tensor = output_tensor[[2, 1, 0], :, :].cpu().float() * 0.5 + 0.5  # Convert BGR back to RGB
    output_image = transforms.ToPILImage()(output_tensor)
    output_image.save("styled_output.jpg")
    print("Styled image saved as styled_output.jpg")

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    print("Choose a style:")
    for i, style in enumerate(STYLE_CHOICE_LIST, 1):
        print(f"{i}. {style}")
    choice = int(input("Enter style number: ")) - 1
    apply_style(image_path, STYLE_CHOICE_LIST[choice])
