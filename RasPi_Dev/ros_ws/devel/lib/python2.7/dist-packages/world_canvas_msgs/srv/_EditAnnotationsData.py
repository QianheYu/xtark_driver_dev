# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from world_canvas_msgs/EditAnnotationsDataRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import world_canvas_msgs.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class EditAnnotationsDataRequest(genpy.Message):
  _md5sum = "41ee6a631a74d3fee28d7fa0847f92d3"
  _type = "world_canvas_msgs/EditAnnotationsDataRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """





uint8 NEW=0
uint8 EDIT=1

uint8 action

Annotation annotation
AnnotationData data

================================================================================
MSG: world_canvas_msgs/Annotation
# Annotation: a generic descriptor for an element (object) in a semantic map
# An annotation can be used to introspect, visualize or key into database filters/searches without
# having to touch the described object directly
#  - timestamp : Creation/last update time
#  - world     : World the object belongs to
#  - id        : Annotation unique id
#  - data_id   : Referenced object unique id (an object can be reference by 1 or more annotations)
#  - name      : Referenced object name
#  - type      : Referenced object type (a message type, as world canvas objects are ROS messages)
#  - shape     : One of 1 (CUBE), 2 (SPHERE), 3 (CYLINDER), 9 (TEXT)
#  - color     : R, G, B, A (optional)
#  - size      : X, Y, Z (optional)
#  - keywords  : Generic properties of this object: allows basic filtering without introspecting
#                the object itself
#  - relationships : List of associated annotations, used for retrieving operational sets of objects

# General properties
time timestamp
uuid_msgs/UniqueID id
uuid_msgs/UniqueID data_id
string world
string name
string type

# Physical properties
int32  shape
std_msgs/ColorRGBA color
geometry_msgs/Vector3 size
geometry_msgs/PoseWithCovarianceStamped pose

# Querying properties
string[] keywords
uuid_msgs/UniqueID[] relationships

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/PoseWithCovarianceStamped
# This expresses an estimated pose with a reference coordinate frame and timestamp

Header header
PoseWithCovariance pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: world_canvas_msgs/AnnotationData
# Data for an element in a semantic map stored as a byte array generated by ros::serialization
# These objects are unique, although they can be referenced by one or more annotations
#  - id   : Object unique id; data_id field on Annotation messages point to this uuid
#  - type : Object type; duplicated from annotation for convenience on deserialization
#  - data : Serialized data
uuid_msgs/UniqueID id
string type
uint8[] data
"""
  # Pseudo-constants
  NEW = 0
  EDIT = 1

  __slots__ = ['action','annotation','data']
  _slot_types = ['uint8','world_canvas_msgs/Annotation','world_canvas_msgs/AnnotationData']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       action,annotation,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EditAnnotationsDataRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.action is None:
        self.action = 0
      if self.annotation is None:
        self.annotation = world_canvas_msgs.msg.Annotation()
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
    else:
      self.action = 0
      self.annotation = world_canvas_msgs.msg.Annotation()
      self.data = world_canvas_msgs.msg.AnnotationData()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B2I().pack(_x.action, _x.annotation.timestamp.secs, _x.annotation.timestamp.nsecs))
      _x = self.annotation.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.annotation.data_id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.annotation.world
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.annotation.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.annotation.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_i4f3d3I().pack(_x.annotation.shape, _x.annotation.color.r, _x.annotation.color.g, _x.annotation.color.b, _x.annotation.color.a, _x.annotation.size.x, _x.annotation.size.y, _x.annotation.size.z, _x.annotation.pose.header.seq, _x.annotation.pose.header.stamp.secs, _x.annotation.pose.header.stamp.nsecs))
      _x = self.annotation.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.annotation.pose.pose.pose.position.x, _x.annotation.pose.pose.pose.position.y, _x.annotation.pose.pose.pose.position.z, _x.annotation.pose.pose.pose.orientation.x, _x.annotation.pose.pose.pose.orientation.y, _x.annotation.pose.pose.pose.orientation.z, _x.annotation.pose.pose.pose.orientation.w))
      buff.write(_get_struct_36d().pack(*self.annotation.pose.pose.covariance))
      length = len(self.annotation.keywords)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation.keywords:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.annotation.relationships)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation.relationships:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
      _x = self.data.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.data.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.annotation is None:
        self.annotation = world_canvas_msgs.msg.Annotation()
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.action, _x.annotation.timestamp.secs, _x.annotation.timestamp.nsecs,) = _get_struct_B2I().unpack(str[start:end])
      start = end
      end += 16
      self.annotation.id.uuid = str[start:end]
      start = end
      end += 16
      self.annotation.data_id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.world = str[start:end].decode('utf-8')
      else:
        self.annotation.world = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.name = str[start:end].decode('utf-8')
      else:
        self.annotation.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.type = str[start:end].decode('utf-8')
      else:
        self.annotation.type = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.annotation.shape, _x.annotation.color.r, _x.annotation.color.g, _x.annotation.color.b, _x.annotation.color.a, _x.annotation.size.x, _x.annotation.size.y, _x.annotation.size.z, _x.annotation.pose.header.seq, _x.annotation.pose.header.stamp.secs, _x.annotation.pose.header.stamp.nsecs,) = _get_struct_i4f3d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.annotation.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.annotation.pose.pose.pose.position.x, _x.annotation.pose.pose.pose.position.y, _x.annotation.pose.pose.pose.position.z, _x.annotation.pose.pose.pose.orientation.x, _x.annotation.pose.pose.pose.orientation.y, _x.annotation.pose.pose.pose.orientation.z, _x.annotation.pose.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.annotation.pose.pose.covariance = _get_struct_36d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation.keywords = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.annotation.keywords.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation.relationships = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation.relationships.append(val1)
      start = end
      end += 16
      self.data.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data.type = str[start:end].decode('utf-8')
      else:
        self.data.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.data.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B2I().pack(_x.action, _x.annotation.timestamp.secs, _x.annotation.timestamp.nsecs))
      _x = self.annotation.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.annotation.data_id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.annotation.world
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.annotation.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.annotation.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_i4f3d3I().pack(_x.annotation.shape, _x.annotation.color.r, _x.annotation.color.g, _x.annotation.color.b, _x.annotation.color.a, _x.annotation.size.x, _x.annotation.size.y, _x.annotation.size.z, _x.annotation.pose.header.seq, _x.annotation.pose.header.stamp.secs, _x.annotation.pose.header.stamp.nsecs))
      _x = self.annotation.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.annotation.pose.pose.pose.position.x, _x.annotation.pose.pose.pose.position.y, _x.annotation.pose.pose.pose.position.z, _x.annotation.pose.pose.pose.orientation.x, _x.annotation.pose.pose.pose.orientation.y, _x.annotation.pose.pose.pose.orientation.z, _x.annotation.pose.pose.pose.orientation.w))
      buff.write(self.annotation.pose.pose.covariance.tostring())
      length = len(self.annotation.keywords)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation.keywords:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.annotation.relationships)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation.relationships:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
      _x = self.data.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.data.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.annotation is None:
        self.annotation = world_canvas_msgs.msg.Annotation()
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
      end = 0
      _x = self
      start = end
      end += 9
      (_x.action, _x.annotation.timestamp.secs, _x.annotation.timestamp.nsecs,) = _get_struct_B2I().unpack(str[start:end])
      start = end
      end += 16
      self.annotation.id.uuid = str[start:end]
      start = end
      end += 16
      self.annotation.data_id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.world = str[start:end].decode('utf-8')
      else:
        self.annotation.world = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.name = str[start:end].decode('utf-8')
      else:
        self.annotation.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.type = str[start:end].decode('utf-8')
      else:
        self.annotation.type = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.annotation.shape, _x.annotation.color.r, _x.annotation.color.g, _x.annotation.color.b, _x.annotation.color.a, _x.annotation.size.x, _x.annotation.size.y, _x.annotation.size.z, _x.annotation.pose.header.seq, _x.annotation.pose.header.stamp.secs, _x.annotation.pose.header.stamp.nsecs,) = _get_struct_i4f3d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.annotation.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.annotation.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.annotation.pose.pose.pose.position.x, _x.annotation.pose.pose.pose.position.y, _x.annotation.pose.pose.pose.position.z, _x.annotation.pose.pose.pose.orientation.x, _x.annotation.pose.pose.pose.orientation.y, _x.annotation.pose.pose.pose.orientation.z, _x.annotation.pose.pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      start = end
      end += 288
      self.annotation.pose.pose.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation.keywords = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.annotation.keywords.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation.relationships = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation.relationships.append(val1)
      start = end
      end += 16
      self.data.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data.type = str[start:end].decode('utf-8')
      else:
        self.data.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.data.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i4f3d3I = None
def _get_struct_i4f3d3I():
    global _struct_i4f3d3I
    if _struct_i4f3d3I is None:
        _struct_i4f3d3I = struct.Struct("<i4f3d3I")
    return _struct_i4f3d3I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_16B = None
def _get_struct_16B():
    global _struct_16B
    if _struct_16B is None:
        _struct_16B = struct.Struct("<16B")
    return _struct_16B
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_16s = None
def _get_struct_16s():
    global _struct_16s
    if _struct_16s is None:
        _struct_16s = struct.Struct("<16s")
    return _struct_16s
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from world_canvas_msgs/EditAnnotationsDataResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import world_canvas_msgs.msg

class EditAnnotationsDataResponse(genpy.Message):
  _md5sum = "f3d451f2a08e1dc3084d378560b01c8e"
  _type = "world_canvas_msgs/EditAnnotationsDataResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 UPDATE=10
uint8 DELETE=12
uint8 CANCEL=13

uint8 action

AnnotationData data

================================================================================
MSG: world_canvas_msgs/AnnotationData
# Data for an element in a semantic map stored as a byte array generated by ros::serialization
# These objects are unique, although they can be referenced by one or more annotations
#  - id   : Object unique id; data_id field on Annotation messages point to this uuid
#  - type : Object type; duplicated from annotation for convenience on deserialization
#  - data : Serialized data
uuid_msgs/UniqueID id
string type
uint8[] data

================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid
"""
  # Pseudo-constants
  UPDATE = 10
  DELETE = 12
  CANCEL = 13

  __slots__ = ['action','data']
  _slot_types = ['uint8','world_canvas_msgs/AnnotationData']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       action,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(EditAnnotationsDataResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.action is None:
        self.action = 0
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
    else:
      self.action = 0
      self.data = world_canvas_msgs.msg.AnnotationData()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.action))
      _x = self.data.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.data.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
      end = 0
      start = end
      end += 1
      (self.action,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 16
      self.data.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data.type = str[start:end].decode('utf-8')
      else:
        self.data.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.data.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.action))
      _x = self.data.id.uuid
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_16B().pack(*_x))
      else:
        buff.write(_get_struct_16s().pack(_x))
      _x = self.data.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.data.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.data is None:
        self.data = world_canvas_msgs.msg.AnnotationData()
      end = 0
      start = end
      end += 1
      (self.action,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 16
      self.data.id.uuid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.data.type = str[start:end].decode('utf-8')
      else:
        self.data.type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.data.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_16B = None
def _get_struct_16B():
    global _struct_16B
    if _struct_16B is None:
        _struct_16B = struct.Struct("<16B")
    return _struct_16B
_struct_16s = None
def _get_struct_16s():
    global _struct_16s
    if _struct_16s is None:
        _struct_16s = struct.Struct("<16s")
    return _struct_16s
class EditAnnotationsData(object):
  _type          = 'world_canvas_msgs/EditAnnotationsData'
  _md5sum = '457c97e1836c61682d0f4bb2f4defba9'
  _request_class  = EditAnnotationsDataRequest
  _response_class = EditAnnotationsDataResponse
