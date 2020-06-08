# Mask r-cnn tutorial #
P.S. подразумевается, что вы используете среду *Anaconda* для реализации от matterport

Этот репозиторий ещё не доделан

### Подготовка: ###

Для начала просмотрите requirements.txt

Давайте посмотрим на структуру проекта:

```
---Projetc:
  ---models:
    ---....
    ---research:
      ---....
      ---oblect_detection:
        ---train.py
        ---xml_to_csv.py
        ---generate_tfrecord.py
        ---images
        ---....
  ---labelImg.exe
  ---delete.py
  ---converte.py
```
  

### Начало работы: ###

Для начала соберем датасет. Лично я для этого использую поисковую выдачу яндекса, но ни кто не мешает использовать что-то другое.

Алгоритм действий:
1) Ищем изображения
2) Через Chrome сохраняем страницу с выдачей(полностью)
3) Находим папку с материалами страницы
4) Удаляем все лишние элементы(должны остаться: i, i(1), i(2)...)
5) Скачайте файл *convertor.py* в дерикторию с папкой
6) Запустите файл

После этих действий необходимо удостовериться, что в папке нет копий. Для этого скачайте файл *delete.py* и повторите шаги 5,6.

### Аннотрирование: ###

#### Один из вариантов для реализации от matterport: ####

Теперь приступим к аннотированию изображений. Я предпочитаю использовать веб-инструмент VIA (VGG Image Annotator).

https://www.cs.bgu.ac.il/~drobya/annotation.html - VIA.

На главной странице можно увидеть "Getting Started" - прочитайте его. Скачайте файл в формате *json* строки(Annotation => Save as JSON)

#### Мы же используем labelImg.exe из этого репозитория: ####

Ипользуйте этот инструмент. После каждого аннотирования изображения и сохраните его, как показано на картинке:

![Image alt](https://github.com/Lednik7/Mask-r-cnn/raw/master/images/Screenshot_6.png)

### Prepoccesing: ###

1) Для начала давайте скачаем [репозиторий](https://github.com/tensorflow/models) в каталог с нашим проектом
2)

**Больше информации:**

https://engineering.matterport.com/splash-of-color-instance-segmentation-with-mask-r-cnn-and-tensorflow-7c761e238b46

https://github.com/matterport/Mask_RCNN

https://www.youtube.com/watch?v=-lIVq52AAPc&list=PL7MfTiaPHGdFIqw16GLMsLKrrly8FtN91

https://www.youtube.com/watch?v=dM_LPsgMe84&list=PL4_hYwCyhAvZeq93ssEUaR47xhvs7IhJM&index=13
