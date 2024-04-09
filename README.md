# 慧眼智鉴——智能垃圾分类
## 主要功能：
（1）输入图片后基于我国现行垃圾分类标准指出属于哪一类垃圾  
（2）支持语音及文字输入查询垃圾属于哪一类   
（3）实现对某一特定领域的垃圾分类  
（4）使用户可以基于我们预训练的模型，实现输入图片及分类后的自训练，可以自定义垃圾的类别用于具体领域。  
（5）提供垃圾回收建议：除了简单地识别垃圾类别外，我们可以根据用户提供的垃圾种类，向其提供相关的垃圾回收和处理建议  
## 扩展功能：
（1）允许用户对分类结果进行反馈，并提供正确分类的参考。我们将用户反馈更新到模型中，帮助改进我们的模型和算法，提高分类准确度和稳定性。    
（2）结合手机相机和AR技术，提供实时的垃圾分类指导。用户可以通过手机相机拍摄垃圾，系统可以实时识别垃圾类型。    
（3）根据用户的垃圾分类历史和偏好，提供个性化的垃圾分类推荐。例如，根据用户的地理位置、垃圾种类偏好和生活习惯，推荐适合用户的垃圾分类方案和处理方法。      
（4）创建一个基于用户垃圾分类行为的环保成就系统。根据用户参与垃圾分类的频率、准确性和贡献度等指标，给予用户相应的环保成就称号或奖励。这可以激励用户更加积极地参与垃圾分类活动，同时也可以增强用户对环保事业的认同感和参与度。    
（5）开发一个垃圾分类教育模块，向用户传播垃圾分类知识和技能。通过文字、图片、视频等多种形式，向用户介绍不同类型垃圾的特点、分类方法和处理方式，以及垃圾分类的环保意义和社会影响。    
## 技术路线
使用Python语言编程，对于图片分类，采用opencv + torchvision的图片处理技术，使用pytorch进行深度学习模型的训练。目前计划使用的模型是 ResNet50，后续也会考虑准确率等因素加入其他模型。算法方面，采用交叉熵损失函数，优化器选择 Adam，并采用 StepLR 进行学习率衰减。架构方面，采用Flask-Django作为前后端接口进行前后端分离设计，后端以python为主，前端主要采用vue框架。在用户数据方面，采用MySQL作为数据库进行数据的存储与处理。  
## 参考代码
目前在github上能找到的垃圾分类模型很少，而且大多已经过时难以使用。但是关于垃圾分类的数据集能找到很多。  
数据集：  
[垃圾分类数据集at飞桨at](https://aistudio.baidu.com/aistudio/datasetdetail/30982)

[垃圾分类数据集at Github](https://github.com/GuoHuiTian/GarbageSortingPictureDataSet.git)

参考代码:  
[https://github.com/Jack-Cherish/Deep-Learning/tree/master/Pytorch-Seg/lesson-4](https://github.com/Jack-Cherish/Deep-Learning/tree/master/Pytorch-Seg/lesson-4)
## 提升及修改：
（1）升级代码架构，使代码适合现在的开发环境，能够正常运行。  
（2）修改模型的功能，使之分类结果与中国现行标准相符合。  
（3）实现对某一特定领域的垃圾分类。  
（4）使用户可以基于我们预训练的模型，实现输入图片及分类后的自训练，可以自定义垃圾的类别用于具体领域。  
（5）提供垃圾回收建议：除了简单地识别垃圾类别外，我们可以根据用户提供的垃圾种类，向其提供相关的垃圾回收和处理建议。  
（6）所有的扩展功能  
