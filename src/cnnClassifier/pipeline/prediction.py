import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
        # Load model once during initialization
        try:
            self.model = load_model(os.path.join("artifacts", "training", "model.h5"))
            # Try to compile, but don't fail if it doesn't work
            try:
                self.model.compile(
                    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                    loss=tf.keras.losses.CategoricalCrossentropy(),
                    metrics=["accuracy"]
                )
            except Exception as e:
                print(f"Warning: Could not recompile model: {e}")
                # Model might still work without recompilation
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None


    
    def predict(self):
        if self.model is None:
            return [{"error": "Model not loaded"}]
            
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(self.model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]