from keras.layers import Conv2D, Conv3D, LeakyReLU, Conv2DTranspose, Conv3DTranspose, concatenate, MaxPooling2D, MaxPooling3D, Lambda, BatchNormalization, add
from keras.regularizers import l1_l2
from keras import backend as K


def samplingDense(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], K.shape(z_mean)[1]), mean=0., stddev=1.0)
    return z_mean + K.exp(z_log_var) * epsilon


def samplingConv(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], K.shape(z_mean)[1]), mean=0., stddev=1.0)
    return Lambda(lambda input:input[:, :, 0, 0])(z_mean) + K.exp(Lambda(lambda input:input[:, :, 0, 0])(z_log_var)) * epsilon


def fCreateLeakyReluConv2D(filters, kernel_size=(3, 3), strides=(1, 1), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        conv2d = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        return LeakyReLU()(conv2d)
    return f


def fCreateLeakyReluBNConv2D(filters, kernel_size=(3, 3), strides=(1, 1), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        output = BatchNormalization(axis=1)(output)

        return LeakyReLU()(output)
    return f


def fCreateLeakyReluConv3D(filters, kernel_size=(3, 3, 3), strides=(1, 1, 1), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        conv3d = Conv3D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        return LeakyReLU()(conv3d)
    return f


def fCreateLeakyReluBNConv3D(filters, kernel_size, strides, padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        conv3d = Conv3D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        return BatchNormalization(axis=1)(LeakyReLU()(conv3d))
    return f


def fCreateConv2D_ResBlock(filters, kernel_size=(3, 3), strides=(2, 2), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        skip = LeakyReLU()(output)

        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(skip)
        output = LeakyReLU()(output)

        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(output)
        output = LeakyReLU()(output)

        output = add([skip, output])
        return output
    return f

def fCreateConv3D_ResBlock(filters, kernel_size=(3, 3, 2), strides=(2, 2, 1), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv3D(filters,
                        kernel_size=kernel_size,
                        strides=strides,
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        skip = LeakyReLU()(output)

        output = Conv3D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(skip)
        output = LeakyReLU()(output)

        output = Conv3D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(output)
        output = LeakyReLU()(output)

        output = add([skip, output])
        return output
    return f

def fCreateConv2DTranspose_ResBlock(filters, kernel_size=(3, 3), strides=(2, 2), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv2DTranspose(filters=filters,
                                 kernel_size=kernel_size,
                                 strides=strides,
                                 padding=padding,
                                 kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        skip = LeakyReLU()(output)

        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(skip)
        output = LeakyReLU()(output)

        output = Conv2D(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(output)
        output = LeakyReLU()(output)

        output = add([skip, output])

        return output
    return f


def fCreateConv3DTranspose_ResBlock(filters, kernel_size=(3, 3, 1), strides=(2, 2, 1), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv3DTranspose(filters=filters,
                                 kernel_size=kernel_size,
                                 strides=strides,
                                 padding=padding,
                                 kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        skip = LeakyReLU()(output)

        output = Conv3DTranspose(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(skip)
        output = LeakyReLU()(output)

        output = Conv3DTranspose(filters,
                        kernel_size=kernel_size,
                        strides=(1, 1, 1),
                        padding=padding,
                        kernel_regularizer=l1_l2(l1_reg, l2_reg))(output)
        output = LeakyReLU()(output)

        output = add([skip, output])

        return output
    return f

def fCreateConv2DTranspose(filters, strides, kernel_size=(3, 3), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        conv2d = Conv2DTranspose(filters=filters,
                                 kernel_size=kernel_size,
                                 strides=strides,
                                 padding=padding,
                                 kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)

        return LeakyReLU()(conv2d)
    return f


def fCreateConv2DBNTranspose(filters, strides, kernel_size=(3, 3), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        output = Conv2DTranspose(filters=filters,
                                 kernel_size=kernel_size,
                                 strides=strides,
                                 padding=padding,
                                 kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)

        output = BatchNormalization(axis=1)(output)
        return LeakyReLU()(output)
    return f


def fCreateConv3DTranspose(filters, strides, kernel_size=(4, 4, 2), padding='same'):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        conv2d = Conv3DTranspose(filters=filters,
                                 kernel_size=kernel_size,
                                 strides=strides,
                                 padding=padding,
                                 kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)

        return LeakyReLU()(conv2d)
    return f


def fCreateConv2D_InceptionBlock(filters):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        # branch 1x1
        branch_1 = Conv2D(filters=filters[0],
                          kernel_size=(1, 1),
                          strides=(1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_1 = LeakyReLU()(branch_1)

        # branch 3x3
        branch_3 = Conv2D(filters=filters[0],
                          kernel_size=(1, 1),
                          strides=(1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_3 = Conv2D(filters=filters[2],
                          kernel_size=(3, 3),
                          strides=(1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_3)
        branch_3 = LeakyReLU()(branch_3)

        # branch 5x5
        branch_5 = Conv2D(filters=filters[0],
                          kernel_size=(1, 1),
                          strides=(1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_5 = Conv2D(filters=filters[1],
                          kernel_size=(5, 5),
                          strides=(1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_5)
        branch_5 = LeakyReLU()(branch_5)

        # branch maxpooling
        branch_pool = MaxPooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inputs)
        branch_pool = Conv2D(filters=filters[0],
                             kernel_size=(1, 1),
                             strides=(1, 1),
                             padding='same',
                             kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_pool)
        branch_pool = LeakyReLU()(branch_pool)

        # concatenate branches together
        out = concatenate([branch_1, branch_3, branch_5, branch_pool], axis=1)
        return out
    return f

def fCreateConv3D_InceptionBlock(filters):
    l1_reg = 0
    l2_reg = 1e-6

    def f(inputs):
        # branch 1x1
        branch_1 = Conv3D(filters=filters[0],
                          kernel_size=(1, 1, 1),
                          strides=(1, 1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_1 = LeakyReLU()(branch_1)

        # branch 3x3
        branch_3 = Conv3D(filters=filters[0],
                          kernel_size=(1, 1, 1),
                          strides=(1, 1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_3 = Conv3D(filters=filters[2],
                          kernel_size=(3, 3, 3),
                          strides=(1, 1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_3)
        branch_3 = LeakyReLU()(branch_3)

        # branch 5x5
        branch_5 = Conv3D(filters=filters[0],
                          kernel_size=(1, 1, 1),
                          strides=(1, 1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(inputs)
        branch_5 = Conv3D(filters=filters[1],
                          kernel_size=(5, 5, 5),
                          strides=(1, 1, 1),
                          padding='same',
                          kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_5)
        branch_5 = LeakyReLU()(branch_5)

        # branch maxpooling
        branch_pool = MaxPooling3D(pool_size=(3, 3, 3), strides=(1, 1, 1), padding='same')(inputs)
        branch_pool = Conv3D(filters=filters[0],
                             kernel_size=(1, 1, 1),
                             strides=(1, 1, 1),
                             padding='same',
                             kernel_regularizer=l1_l2(l1_reg, l2_reg))(branch_pool)
        branch_pool = LeakyReLU()(branch_pool)

        # concatenate branches together
        out = concatenate([branch_1, branch_3, branch_5, branch_pool], axis=1)
        return out
    return f