import tensorflow as tf
import numpy as np
import time

def im2tfrecord(image, path):
    """
     Takes the image and saves it to a tfrecord
     using image and image.shape info
    """

    # np.frombuffer(np.array(a.shape).tostring(), dtype=int)  # numpy supports string conversion
    image_shape = np.array(image.shape, dtype=np.int32).tostring()
    image = image.astype(np.int16).tostring()

    # create an example protocol buffer
    feature = {
        'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
        'image_shape': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_shape]))
    }
    features = tf.train.Features(feature=feature)
    example = tf.train.Example(features=features)

    with tf.python_io.TFRecordWriter(str(path)) as writer:
        writer.write(example.SerializeToString())

def parse_function(example_proto):
    time1 = time.time()
    features = {
        'image': tf.FixedLenFeature([], tf.string),
        'image_shape': tf.FixedLenFeature([], tf.string),
    }

    content = tf.parse_single_example(example_proto, features=features)

    content['image_shape'] = tf.decode_raw(content['image_shape'], tf.int32)
    content['image'] = tf.decode_raw(content['image'], tf.int16)
    content['image'] = tf.reshape(content['image'], content['image_shape'])
    print('parse using time: ', time.time() - time1)
    return content['image']
