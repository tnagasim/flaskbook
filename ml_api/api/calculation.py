import pickle

import numpy as np
from flask import Response, jsonify

from api.preparation import extract_filenames
from api.preprocess import get_shrunk_img


def evaluate_probs(request) -> Response:
    """テストデータを利用してロジスティック回帰の学習済みモデルのアウトプットを評価"""
    file_id = request.json["file_id"]
    filenames = extract_filenames(file_id)
    if type(filenames) is tuple:
        response, _ = filenames
        return response
    if type(filenames) is not list:
        raise
    img_test = get_shrunk_img(filenames)

    with open("model.pickle", mode="rb") as fp:
        model = pickle.load(fp)

    X_true = np.array([int(filename[:1]) for filename in filenames])

    predicted_result = model.predict(img_test).tolist()
    accuracy = model.score(img_test, X_true)
    observed_result = X_true.tolist()

    return jsonify(
        {
            "results": {
                "file_id": file_id,
                "observed_result": observed_result,
                "predicted_result": predicted_result,
                "accuracy": accuracy,
            }
        },
        201,
    )
