# Anime Background Style Transfer

This project applies anime-style background transfer to images using pre-trained models inspired by famous anime directors. The models are sourced from Hugging Face and can generate stylized images in the styles of Makoto Shinkai, Mamoru Hosoda, Hayao Miyazaki, and Satoshi Kon.

## Features

- Transforms images into anime-style backgrounds
- Supports four different anime styles
- Utilizes pre-trained models from Hugging Face
- Runs on CPU or GPU

## Installation

Ensure you have Python installed. Then, install the required dependencies:

```bash
pip install torch torchvision numpy pillow huggingface_hub
```

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/iamrukeshduwal/Anime-Background-Style-Transfer.git
   cd Anime-Background-Style-Transfer
   ```

2. Run the script:

   ```bash
   python test.py
   ```

3. Enter the path of the image you want to stylize.

4. Choose a style from the provided options:

   - Makoto Shinkai
   - Mamoru Hosoda
   - Hayao Miyazaki
   - Satoshi Kon

5. The stylized image will be saved as `styled_output.jpg`.

## Model Sources

The models used in this project are sourced from Hugging Face:

- [AnimeBackgroundGAN - Shinkai](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Shinkai)
- [AnimeBackgroundGAN - Hosoda](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Hosoda)
- [AnimeBackgroundGAN - Miyazaki](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Miyazaki)
- [AnimeBackgroundGAN - Kon](https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Kon)

## Acknowledgments

This project is inspired by [AnimeBackgroundGAN](https://huggingface.co/spaces/akiyamasho/AnimeBackgroundGAN) on Hugging Face. The models and reference code are taken from the Hugging Face Git repository, with modifications for this implementation.

## License

This project is open-source and available under the MIT License.

