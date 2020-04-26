; Auto-generated. Do not edit!


(cl:in-package hector_uav_msgs-msg)


;//! \htmlinclude TakeoffFeedback.msg.html

(cl:defclass <TakeoffFeedback> (roslisp-msg-protocol:ros-message)
  ((current_pose
    :reader current_pose
    :initarg :current_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass TakeoffFeedback (<TakeoffFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TakeoffFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TakeoffFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hector_uav_msgs-msg:<TakeoffFeedback> is deprecated: use hector_uav_msgs-msg:TakeoffFeedback instead.")))

(cl:ensure-generic-function 'current_pose-val :lambda-list '(m))
(cl:defmethod current_pose-val ((m <TakeoffFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hector_uav_msgs-msg:current_pose-val is deprecated.  Use hector_uav_msgs-msg:current_pose instead.")
  (current_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TakeoffFeedback>) ostream)
  "Serializes a message object of type '<TakeoffFeedback>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'current_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TakeoffFeedback>) istream)
  "Deserializes a message object of type '<TakeoffFeedback>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'current_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TakeoffFeedback>)))
  "Returns string type for a message object of type '<TakeoffFeedback>"
  "hector_uav_msgs/TakeoffFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TakeoffFeedback)))
  "Returns string type for a message object of type 'TakeoffFeedback"
  "hector_uav_msgs/TakeoffFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TakeoffFeedback>)))
  "Returns md5sum for a message object of type '<TakeoffFeedback>"
  "dd7058fae6e1bf2400513fe092a44c92")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TakeoffFeedback)))
  "Returns md5sum for a message object of type 'TakeoffFeedback"
  "dd7058fae6e1bf2400513fe092a44c92")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TakeoffFeedback>)))
  "Returns full string definition for message of type '<TakeoffFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/PoseStamped current_pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TakeoffFeedback)))
  "Returns full string definition for message of type 'TakeoffFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/PoseStamped current_pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TakeoffFeedback>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'current_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TakeoffFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'TakeoffFeedback
    (cl:cons ':current_pose (current_pose msg))
))