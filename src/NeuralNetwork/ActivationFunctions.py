try:
    from cython import compiled
except ImportError as e:
    compiled = False

if not compiled:
    from math import exp, tanh, atan, asinh, sqrt
    globals()["_exp"] = exp
    globals()["_tanh"] = tanh
    globals()["_atan"] = atan
    globals()["_asinh"] = asinh
    globals()["_sqrt"] = sqrt


def identity(x):
    return x


def binaryStep(x):
    if x < 0:
        return 0
    if x >= 0:
        return 1


def sigmoid(x):
    return 1/(1+_exp(-x))


def tanH(x):
    return _tanh(x)


def sqnl(x):
    if x > 2.0:
        return 1
    elif 0 <= x <= 2.0:
        return x - ((x ** 2) / 4)
    elif - 2.0 <= x < 0:
        return x + ((x ** 2) / 4)
    elif x < -2.0:
        return -1


def arcTan(x):
    return _atan(x)


def arcSinH(x):
    return _asinh(x)


def elliotSig(x):
    return x/(1+abs(x))


def inverseSquareRoot(x, a=1):
    return x/_sqrt(1+(a*(x**2)))


def piecewiseLinear(x, a=0.1, b=1):
    return max(a*(x+b)-b, min(a*(x-b)+b, x))


def rectifiedLinear(x):
    if x <= 0:
        return 0
    else:
        return x


def bipolarRectifiedLinear(x):
    if x % 2 == 0:
        return rectifiedLinear(x)
    else:
        return (-rectifiedLinear(-x))


def leakyRectifiedLinear(x):
    if x < 0:
        return 0.001 * x
    else:
        return x


def parametricRectifiedLinear(x, a=0.5):
    if x < 0:
        return a * x
    else:
        return x


def exponentialLinear(x, a=1):
    if x <= 0:
        return a * (_exp(x) - 1)
    else:
        return x


def scaledExponentialLinear(x, a=1.673):
    if x < 0:
        return 1.0507 * (a * (_exp(x) - 1))
    else:
        return x
