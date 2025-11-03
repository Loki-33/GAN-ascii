# GAN-ascii

A GAN model pix2pix style, to generate ascii images

## ARCHITECTURE
1. Generator: U-NET model
2. Discriminator: PatchGAN

### OVERVIEW
My dataset contained only 1000 images which i converted to ascii using the "ascii_generator.py" code. <br>
I tried training with different values of lam(100, 80, 60) each for epoch 100, the best result was for epoch 80 but it wasn't that great, everything was blurry. <br>
I even tried lower values for lamda to prioritize clarity of images but it didn't help eihter. <br>

So my conlusion is:
1. The dataset was too small
2. More longer trianing needed
3. And maube more tuning of hyperparameters
 
