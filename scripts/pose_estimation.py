from tf_pose_estimation.src.estimator import TfPoseEstimator
from tf_pose_estimation.src.networks import get_graph_path, model_wh


class PoseEstimation:
    def __init__(self, model='mobilenet_thin', resolution='432x368'):
        w, h = model_wh(resolution)
        self.e = TfPoseEstimator(get_graph_path(model), target_size=(w, h))

    def detect(self, image):
        output = []
        humans = self.e.inference(image)
        for human in humans:
            parts = dict()
            for key, part in human.body_parts.items():
                part = human.body_parts[key]
                parts[key] = (part.x, part.y)
            output.append(parts)
        return output
