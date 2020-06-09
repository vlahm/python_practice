import tensorflow as tf
# import numpy as np

mnist = tf.keras.datasets.mnist

#convert from int to float (why is mnist stored as int??)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

#stack model layers
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

#get scores for each example
predictions = model(x_train[:1]).numpy()

#convert them from log-odds (logit) to "probabilities" using softmax.
#don't bake this into the model, as it hinders inter-model comparison
tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

rrr = np.array([[11, 22], [33, 44], [55, 66]])
# index data
print(rrr[:,0])
print(rrr[0,0])

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

probability_model(x_test[:5])
