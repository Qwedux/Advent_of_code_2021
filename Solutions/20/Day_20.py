import numpy as np
input_file ="sample.txt" if 0 else "input.txt"

with open(input_file) as inp:
    algo, _, *image = [[0 if cell == '.' else 1 for cell in row] for row in inp.read().split('\n')]
    image = np.array(image)
    mapa = np.zeros((350, 350), dtype=int)
    mapa[125:125+image.shape[0], 125:125+image.shape[1]] = image
    
    def convo(img):
        return np.stack((
            img[0:-2, 0:-2], img[0:-2, 1:-1], img[0:-2, 2:  ],
            img[1:-1, 0:-2], img[1:-1, 1:-1], img[1:-1, 2:  ],
            img[2:  , 0:-2], img[2:  , 1:-1], img[2:  , 2:  ]
        ), axis=-1)
    
    def apply_iter(img):
        img = convo(img)
        res = np.zeros(img.shape[:2], dtype=int)
        for row in range(img.shape[0]):
            for col in range(img.shape[1]):
                index = int(''.join([str(x) for x in img[row][col]]), 2)
                res[row][col] = algo[index]
        return res
    
    def fancyprint(arr):
        print('\n'.join([''.join(['#' if cell else '.' for cell in row]) for row in arr]))
    
    # print(mapa[24:26+image.shape[0], 24:26+image.shape[1]])
    # print(convo(mapa[24:26+image.shape[0], 24:26+image.shape[1]]))
    # fancyprint(apply_iter(apply_iter(mapa))[19:29+image.shape[0], 19:29+image.shape[1]])
    # print(np.sum(apply_iter(apply_iter(mapa))))

    for iters in range(1, 51):
        mapa = apply_iter(mapa)
        if iters in (2, 50):
            print(np.sum(mapa))