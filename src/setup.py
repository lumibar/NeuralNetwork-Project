from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

print(find_packages())
setup(
    name="NEAT_Sim",
    ext_modules=cythonize([
        Extension("NeuralNetwork", ["NeuralNetwork/__init__.py"]),
        Extension("NeuralNetwork.Network", ["NeuralNetwork/Network.py"]),
        Extension("NeuralNetwork.ActivationFunctions", [
                  "NeuralNetwork/ActivationFunctions.py"]),
        Extension("NeuralNetwork.Genes", ["NeuralNetwork/Genes.py"])])
)
