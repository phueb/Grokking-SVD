import numpy as np
from typing import Tuple, Callable


def get_width_height_pixels(collection_id: int,
                            ) -> Tuple[int, int]:
    if collection_id == 0:
        return 400, 300
    elif collection_id == 1:
        return 400, 300
    else:
        return 400, 300


def load_collection(collection_id: int,
                    ) -> Tuple[np.array, Callable[[np.array, int], np.array]]:

    if collection_id == 0:
        __ = 0
        _1 = 10
        _2 = 10
        _3 = 10
        co_mat_original = np.array([
            [_2, __, __, __, __, __, _3, __, __],
            [__, _2, __, __, __, __, _3, __, __],
            [__, __, _2, __, __, __, _3, __, __],
            [__, __, __, _2, __, __, _3, __, __],
            [__, __, __, __, _2, __, __, __, __],
            [__, __, __, __, __, _2, __, __, __],
        ])

        def transform(co_mat: np.array,
                      step: int,
                      ) -> np.array:
            res = co_mat.copy()

            res[5, 5] -= step
            res[4, 4] -= step

            res[4, 6] += step
            res[5, 6] += step

            assert res.sum() == co_mat.sum()
            return res

        return co_mat_original, transform

    if collection_id == 1:
        __ = 0
        _1 = 10
        _2 = 10
        _3 = 10
        co_mat_original = np.array([
            [_2, __, __, __, __, __, _3, __, __],
            [__, _2, __, __, __, __, _3, __, __],
            [__, __, _2, __, __, __, _3, __, __],
            [__, __, __, _2, __, __, _3, __, __],
            [__, __, __, __, _2, __, _3, __, __],
            [__, __, __, __, __, _2, _3, __, __],
        ])

        def transform(co_mat: np.array,
                      step: int,
                      ) -> np.array:
            res = co_mat.copy()

            res[5, 5] -= step
            res[4, 4] -= step

            res[4, 0] += step
            res[5, 0] += step

            assert res.sum() == co_mat.sum()
            return res

        return co_mat_original, transform

    if collection_id == 2:
        __ = 0
        _1 = 10
        _2 = 10
        _3 = 10
        co_mat_original = np.array([
            [_2, __, __, __, __, __, __, __, __],
            [__, _2, __, __, __, __, __, __, __],
            [__, __, _2, __, __, __, __, __, __],
            [__, __, __, _2, __, __, __, __, __],
            [__, __, __, __, _2, __, __, __, __],
            [__, __, __, __, __, _2, __, __, __],
        ])

        def transform(co_mat: np.array,
                      step: int,
                      ) -> np.array:
            res = co_mat.copy()

            res[5, 5] -= step
            res[4, 4] -= step

            res[4, 0] += step
            res[5, 0] += step

            assert res.sum() == co_mat.sum()
            return res

        return co_mat_original, transform

    elif collection_id == 3:
        __ = 0
        _1 = 10
        _2 = 10
        _3 = 10
        co_mat_original = np.array([
            [_1, __, __, __, __, __, _3, _2, __],
            [__, _1, __, __, __, __, _3, _2, __],
            [__, __, _1, __, __, __, _3, _2, __],
            [__, __, __, _1, __, __, _3, __, _2],
            [__, __, __, __, _1, __, _3, __, _2],
            [__, __, __, __, __, _1, _3, __, _2],
        ])

        def transform(co_mat: np.array,
                      step: int,
                      ) -> np.array:
            res = co_mat.copy()

            res[0, 7] -= step
            res[1, 7] -= step
            res[2, 7] -= step
            res[3, 8] -= step
            res[4, 8] -= step
            res[5, 8] -= step

            res[:, 6] += step

            assert res.sum() == co_mat.sum()
            return res

        return co_mat_original, transform

    elif collection_id == 4:
        __ = 0
        _1 = 10
        _2 = 10
        _3 = 10
        co_mat_original = np.array([
            [_1, __, __, __, __, __, _3, _2, __],
            [__, _1, __, __, __, __, _3, _2, __],
            [__, __, _1, __, __, __, _3, _2, __],
            [__, __, __, _1, __, __, _3, __, _2],
            [__, __, __, __, _1, __, _3, __, _2],
            [__, __, __, __, __, _1, _3, __, _2],
        ])

        def transform(co_mat: np.array,
                      step: int,
                      ) -> np.array:
            res = co_mat.copy()

            res[0, 0] -= step
            res[1, 1] -= step
            res[2, 2] -= step
            res[3, 3] -= step
            res[4, 4] -= step
            res[5, 5] -= step

            res[:, 6] += step

            assert res.sum() == co_mat.sum()
            return res

        return co_mat_original, transform

    else:
        raise ValueError(f'Did not find collection for id={collection_id}')
