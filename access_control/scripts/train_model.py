import tensorflow as tf
from tensorflow.keras import layers, models

def create_model(input_shape=(224, 224, 3)):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')  # 10 классов для гос. номеров
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

def main():
    # Загрузка данных (здесь нужно использовать ваши данные)
    # train_images, train_labels = load_your_data()

    # Нормализация изображений
    # train_images = train_images / 255.0

    # Создание модели
    model = create_model()

    # Обучение модели
    # model.fit(train_images, train_labels, epochs=10, validation_split=0.2)

    # Сохранение модели
    model.save('models/license_plate_recognition_model')

if __name__ == "__main__":
    main()