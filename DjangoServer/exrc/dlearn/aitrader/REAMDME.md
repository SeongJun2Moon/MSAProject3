# 에러
### Input 0 of layer "sequential" is incompatible with the layer : 차원 변경 에러
```python
x_train = x_train.astype(np.float32).reshape(x_train.shape[0], x_train[1], 1)
```

### ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type int) : 데이터 타입 에러
```python
y_train.astype(np.float32)
```