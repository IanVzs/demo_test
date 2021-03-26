# jupyter中使用paddlex需要设置matplotlib
import matplotlib
matplotlib.use('Agg') 
# 设置使用0号GPU卡（如无GPU，执行此代码后仍然会使用CPU训练模型）
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import paddlex as pdx

from args_tool import data_dir, output_dir

def train():
    from paddlex.cls import transforms
    train_transforms = transforms.Compose([
        transforms.RandomCrop(crop_size=224),
        transforms.RandomHorizontalFlip(),
        transforms.Normalize()
    ])
    eval_transforms = transforms.Compose([
        transforms.ResizeByShort(short_size=256),
        transforms.CenterCrop(crop_size=224),
        transforms.Normalize()
    ])
    
    
    
    train_dataset = pdx.datasets.ImageNet(
        data_dir=f'{data_dir}/mini_imagenet_veg',
        file_list=f'{data_dir}/mini_imagenet_veg/train_list.txt',
        label_list=f'{data_dir}/mini_imagenet_veg/labels.txt',
        transforms=train_transforms)
    eval_dataset = pdx.datasets.ImageNet(
        data_dir=f'{data_dir}/mini_imagenet_veg',
        file_list=f'{data_dir}/mini_imagenet_veg/val_list.txt',
        label_list=f'{data_dir}/mini_imagenet_veg/labels.txt',
        transforms=eval_transforms)
    
    
    
    
    num_classes = len(train_dataset.labels)
    model = pdx.cls.MobileNetV3_large_ssld(num_classes=num_classes)
    model.train(num_epochs=12,
                train_dataset=train_dataset,
                train_batch_size=32,
                eval_dataset=eval_dataset,
                lr_decay_epochs=[6, 8],
                save_interval_epochs=1,
                learning_rate=0.00625,
                save_dir=f'{output_dir}/output/mobilenetv3_large_ssld',
                use_vdl=True)
    
    
def test():
    import paddlex as pdx
    model = pdx.load_model(f'{output_dir}/output/mobilenetv3_large_ssld/best_model')
    image_name = f'{data_dir}/mini_imagenet_veg/mushroom/n07734744_1106.JPEG'
    result = model.predict(image_name)
    print("Predict Result:", result)
    
    
    # lime可解释性可视化
    pdx.interpret.lime(
            f'{data_dir}/mini_imagenet_veg/mushroom/n07734744_1106.JPEG',
            model,
            save_dir=f'{output_dir}/')

if __name__ == "__main__":
    # train()
    test()
