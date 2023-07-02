from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path=r'C:\Users\27786\Desktop\a-PyTorch-Tutorial-to-Image-Captioning-master\dataset_coco.json',
                       image_folder=r'C:\Users\27786\Desktop\a-PyTorch-Tutorial-to-Image-Captioning-master\caption_data',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=r'C:\Users\27786\Desktop\a-PyTorch-Tutorial-to-Image-Captioning-master\caption_data',
                       max_len=50)
