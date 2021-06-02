# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from world_canvas_msgs/GetAnnotationsDataRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg

class GetAnnotationsDataRequest(genpy.Message):
  _md5sum = "fc0f6207fc1c9b03add292ade8ff7951"
  _type = "world_canvas_msgs/GetAnnotationsDataRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

uuid_msgs/UniqueID[] annotation_ids


================================================================================
MSG: uuid_msgs/UniqueID
# A universally unique identifier (UUID).
#
#  http://en.wikipedia.org/wiki/Universally_unique_identifier
#  http://tools.ietf.org/html/rfc4122.html

uint8[16] uuid
"""
  __slots__ = ['annotation_ids']
  _slot_types = ['uuid_msgs/UniqueID[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       annotation_ids

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetAnnotationsDataRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.annotation_ids is None:
        self.annotation_ids = []
    else:
      self.annotation_ids = []

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
      length = len(self.annotation_ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation_ids:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.annotation_ids is None:
        self.annotation_ids = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation_ids = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation_ids.append(val1)
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
      length = len(self.annotation_ids)
      buff.write(_struct_I.pack(length))
      for val1 in self.annotation_ids:
        _x = val1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.annotation_ids is None:
        self.annotation_ids = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.annotation_ids = []
      for i in range(0, length):
        val1 = uuid_msgs.msg.UniqueID()
        start = end
        end += 16
        val1.uuid = str[start:end]
        self.annotation_ids.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
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
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from world_canvas_msgs/GetAnnotationsDataResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import uuid_msgs.msg
import world_canvas_msgs.msg

class GetAnnotationsDataResponse(genpy.Message):
  _md5sum = "5138c2b0e307350745b95b31397311c4"
  _type = "world_canvas_msgs/GetAnnotationsDataResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
bool result
string message

AnnotationData[] data

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
  __slots__ = ['result','message','data']
  _slot_types = ['bool','string','world_canvas_msgs/AnnotationData[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       result,message,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetAnnotationsDataResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.result is None:
        self.result = False
      if self.message is None:
        self.message = ''
      if self.data is None:
        self.data = []
    else:
      self.result = False
      self.message = ''
      self.data = []

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
      buff.write(_get_struct_B().pack(self.result))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _v1 = val1.id
        _x = _v1.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.data
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
        self.data = None
      end = 0
      start = end
      end += 1
      (self.result,) = _get_struct_B().unpack(str[start:end])
      self.result = bool(self.result)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.AnnotationData()
        _v2 = val1.id
        start = end
        end += 16
        _v2.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        self.data.append(val1)
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
      buff.write(_get_struct_B().pack(self.result))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _v3 = val1.id
        _x = _v3.uuid
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(_get_struct_16B().pack(*_x))
        else:
          buff.write(_get_struct_16s().pack(_x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.data
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
        self.data = None
      end = 0
      start = end
      end += 1
      (self.result,) = _get_struct_B().unpack(str[start:end])
      self.result = bool(self.result)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = world_canvas_msgs.msg.AnnotationData()
        _v4 = val1.id
        start = end
        end += 16
        _v4.uuid = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.data = str[start:end]
        self.data.append(val1)
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
class GetAnnotationsData(object):
  _type          = 'world_canvas_msgs/GetAnnotationsData'
  _md5sum = '91d9a7f0b1315b44e207eeb7e9326135'
  _request_class  = GetAnnotationsDataRequest
  _response_class = GetAnnotationsDataResponse
