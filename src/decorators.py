from typing import Callable, TypeVar

F = TypeVar('F',bound=Callable[...,object])

def auditar_operacao(func: F) -> F:
    def wrapper(*args,**kwargs):
        print(f"=> {func.__name__.replace('_',' ').capitalize()}: args={args[1:]} kwargs={kwargs} \n")
        return func(*args,**kwargs)
    return wrapper