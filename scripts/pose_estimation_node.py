#!/usr/bin/env python
import rospy
import json
from pose_estimation import PoseEstimation
from saam_pose_estimation.srv import PoseEstimator, PoseEstimatorResponse
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String


def image_to_cv2(image_message):
    bridge = CvBridge()
    try:
        cv2_image = bridge.imgmsg_to_cv2(
            image_message, desired_encoding="passthrough")
        return cv2_image
    except CvBridgeError as e:
        rospy.logerr(e)


class ROSPoseEstimation:
    def __init__(self):
        self.estimator = PoseEstimation()

    def service_controller(self, req):
        input_image = image_to_cv2(req.input_image)
        result = self.estimator.detect(input_image)
        result = json.dumps(result)
        response = PoseEstimatorResponse()
        response.objects_json = String(result)
        return response


def main():
    rospy.init_node('saam_pose_estimation')

    rospy.loginfo("Initializing estimator ...")
    estimator = ROSPoseEstimation()

    rospy.loginfo("Initializing service ...")
    rospy.Service('saam_pose_estimation', PoseEstimator,
                  estimator.service_controller)

    rospy.loginfo("Ready to estimate bodies.")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.logwarn("Shutting done ...")


if __name__ == "__main__":
    main()
