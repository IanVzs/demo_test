import matplotlib
matplotlib.use('Agg') 
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
        data_dir=f'{data_dir}/vegetables_cls',
        file_list=f'{data_dir}/vegetables_cls/train_list.txt',
        label_list=f'{data_dir}/vegetables_cls/labels.txt',
        transforms=train_transforms,
        shuffle=True)
    eval_dataset = pdx.datasets.ImageNet(
        data_dir=f'{data_dir}/vegetables_cls',
        file_list=f'{data_dir}/vegetables_cls/val_list.txt',
        label_list=f'{data_dir}/vegetables_cls/labels.txt',
        transforms=eval_transforms)
    
    
    num_classes = len(train_dataset.labels)
    model = pdx.cls.MobileNetV2(num_classes=num_classes)
    model.train(num_epochs=10,
                train_dataset=train_dataset,
                train_batch_size=32,
                eval_dataset=eval_dataset,
                lr_decay_epochs=[4, 6, 8],
                save_interval_epochs=1,
                learning_rate=0.025,
                save_dir=f'{output_dir}/mobilenetv2',
                use_vdl=True)
    
def test():
    import paddlex as pdx
    model = pdx.load_model(f'{output_dir}/mobilenetv2/best_model')
    image_name = f'{data_dir}/vegetables_cls/bocai/100.jpg'
    result = model.predict(image_name)
    print("Predict Result:", result)


if __name__ == "__main__":
    # train()
    test()
