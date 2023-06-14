def func_with_args_and_kwargs(*args, **kwargs):
    print(f'Арги:{args}\n Кварги: {kwargs}')

func_with_args_and_kwargs(1,2,c=4,d=8,f=93)