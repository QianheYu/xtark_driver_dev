// Generated by gencpp from file rtabmap_ros/GetMapResponse.msg
// DO NOT EDIT!


#ifndef RTABMAP_ROS_MESSAGE_GETMAPRESPONSE_H
#define RTABMAP_ROS_MESSAGE_GETMAPRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <rtabmap_ros/MapData.h>

namespace rtabmap_ros
{
template <class ContainerAllocator>
struct GetMapResponse_
{
  typedef GetMapResponse_<ContainerAllocator> Type;

  GetMapResponse_()
    : data()  {
    }
  GetMapResponse_(const ContainerAllocator& _alloc)
    : data(_alloc)  {
  (void)_alloc;
    }



   typedef  ::rtabmap_ros::MapData_<ContainerAllocator>  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetMapResponse_

typedef ::rtabmap_ros::GetMapResponse_<std::allocator<void> > GetMapResponse;

typedef boost::shared_ptr< ::rtabmap_ros::GetMapResponse > GetMapResponsePtr;
typedef boost::shared_ptr< ::rtabmap_ros::GetMapResponse const> GetMapResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rtabmap_ros::GetMapResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rtabmap_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'rtabmap_ros': ['/home/xtark/ros_ws/src/vslam/rtabmap_ros/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "be1186efbdcde47a41d62ec7fd4dcf0a";
  }

  static const char* value(const ::rtabmap_ros::GetMapResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbe1186efbdcde47aULL;
  static const uint64_t static_value2 = 0x41d62ec7fd4dcf0aULL;
};

template<class ContainerAllocator>
struct DataType< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rtabmap_ros/GetMapResponse";
  }

  static const char* value(const ::rtabmap_ros::GetMapResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
MapData data\n\
\n\
\n\
================================================================================\n\
MSG: rtabmap_ros/MapData\n\
\n\
Header header\n\
\n\
##################\n\
# Optimized graph\n\
##################\n\
MapGraph graph\n\
\n\
##################\n\
# Graph data\n\
##################\n\
NodeData[] nodes\n\
\n\
\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: rtabmap_ros/MapGraph\n\
\n\
Header header\n\
\n\
##\n\
# /map to /odom transform\n\
# Always identity when the graph is optimized from the latest pose.\n\
##\n\
geometry_msgs/Transform mapToOdom\n\
\n\
# The poses\n\
int32[] posesId\n\
geometry_msgs/Pose[] poses\n\
\n\
# The links\n\
Link[] links\n\
\n\
\n\
\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Transform\n\
# This represents the transform between two coordinate frames in free space.\n\
\n\
Vector3 translation\n\
Quaternion rotation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: rtabmap_ros/Link\n\
#class rtabmap::Link\n\
#{\n\
#   int from;\n\
#   int to;\n\
#   Type type;\n\
#   Transform transform;\n\
#   cv::Mat(6,6,CV_64FC1) information;\n\
#}\n\
\n\
int32 fromId\n\
int32 toId\n\
int32 type\n\
geometry_msgs/Transform transform\n\
float64[36] information\n\
================================================================================\n\
MSG: rtabmap_ros/NodeData\n\
\n\
int32 id\n\
int32 mapId\n\
int32 weight\n\
float64 stamp\n\
string label\n\
\n\
# Pose from odometry not corrected\n\
geometry_msgs/Pose pose\n\
\n\
# Ground truth (optional)\n\
geometry_msgs/Pose groundTruthPose\n\
\n\
# GPS (optional)\n\
GPS gps\n\
\n\
# compressed image in /camera_link frame\n\
# use rtabmap::util3d::uncompressImage() from \"rtabmap/core/util3d.h\"\n\
uint8[] image\n\
\n\
# compressed depth image in /camera_link frame\n\
# use rtabmap::util3d::uncompressImage() from \"rtabmap/core/util3d.h\"\n\
uint8[] depth\n\
\n\
# Camera models\n\
float32[] fx\n\
float32[] fy\n\
float32[] cx\n\
float32[] cy\n\
float32[] width\n\
float32[] height\n\
float32 baseline\n\
# local transform (/base_link -> /camera_link)\n\
geometry_msgs/Transform[] localTransform\n\
\n\
# compressed 2D laser scan in /base_link frame\n\
# use rtabmap::util3d::uncompressData() from \"rtabmap/core/util3d.h\"\n\
uint8[] laserScan\n\
int32 laserScanMaxPts\n\
float32 laserScanMaxRange\n\
int32 laserScanFormat\n\
geometry_msgs/Transform laserScanLocalTransform\n\
\n\
# compressed user data\n\
# use rtabmap::util3d::uncompressData() from \"rtabmap/core/util3d.h\"\n\
uint8[] userData\n\
\n\
# compressed occupancy grid\n\
# use rtabmap::util3d::uncompressData() from \"rtabmap/core/util3d.h\"\n\
uint8[] grid_ground\n\
uint8[] grid_obstacles\n\
uint8[] grid_empty_cells\n\
float32 grid_cell_size\n\
Point3f grid_view_point\n\
\n\
# std::multimap<wordId, cv::Keypoint>\n\
# std::multimap<wordId, pcl::PointXYZ>\n\
int32[] wordIds\n\
KeyPoint[] wordKpts\n\
sensor_msgs/PointCloud2 wordPts\n\
\n\
# compressed descriptors\n\
# use rtabmap::util3d::uncompressData() from \"rtabmap/core/util3d.h\"\n\
uint8[] descriptors\n\
\n\
================================================================================\n\
MSG: rtabmap_ros/GPS\n\
\n\
float64 stamp      # in seconds\n\
float64 longitude  # DD format\n\
float64 latitude   # DD format\n\
float64 altitude   # in meters\n\
float64 error      # in meters\n\
float64 bearing    # North 0->360 deg\n\
================================================================================\n\
MSG: rtabmap_ros/Point3f\n\
#class cv::Point3f\n\
#{\n\
#    float x;\n\
#    float y;\n\
#    float z;\n\
#}\n\
\n\
float32 x\n\
float32 y\n\
float32 z\n\
================================================================================\n\
MSG: rtabmap_ros/KeyPoint\n\
#class cv::KeyPoint\n\
#{\n\
#    Point2f pt;\n\
#    float size;\n\
#    float angle;\n\
#    float response;\n\
#    int octave;\n\
#    int class_id;\n\
#}\n\
\n\
Point2f pt\n\
float32 size\n\
float32 angle\n\
float32 response\n\
int32 octave\n\
int32 class_id\n\
================================================================================\n\
MSG: rtabmap_ros/Point2f\n\
#class cv::Point2f\n\
#{\n\
#    float x;\n\
#    float y;\n\
#}\n\
\n\
float32 x\n\
float32 y\n\
================================================================================\n\
MSG: sensor_msgs/PointCloud2\n\
# This message holds a collection of N-dimensional points, which may\n\
# contain additional information such as normals, intensity, etc. The\n\
# point data is stored as a binary blob, its layout described by the\n\
# contents of the \"fields\" array.\n\
\n\
# The point cloud data may be organized 2d (image-like) or 1d\n\
# (unordered). Point clouds organized as 2d images may be produced by\n\
# camera depth sensors such as stereo or time-of-flight.\n\
\n\
# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n\
# points).\n\
Header header\n\
\n\
# 2D structure of the point cloud. If the cloud is unordered, height is\n\
# 1 and width is the length of the point cloud.\n\
uint32 height\n\
uint32 width\n\
\n\
# Describes the channels and their layout in the binary data blob.\n\
PointField[] fields\n\
\n\
bool    is_bigendian # Is this data bigendian?\n\
uint32  point_step   # Length of a point in bytes\n\
uint32  row_step     # Length of a row in bytes\n\
uint8[] data         # Actual point data, size is (row_step*height)\n\
\n\
bool is_dense        # True if there are no invalid points\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointField\n\
# This message holds the description of one point entry in the\n\
# PointCloud2 message format.\n\
uint8 INT8    = 1\n\
uint8 UINT8   = 2\n\
uint8 INT16   = 3\n\
uint8 UINT16  = 4\n\
uint8 INT32   = 5\n\
uint8 UINT32  = 6\n\
uint8 FLOAT32 = 7\n\
uint8 FLOAT64 = 8\n\
\n\
string name      # Name of field\n\
uint32 offset    # Offset from start of point struct\n\
uint8  datatype  # Datatype enumeration, see above\n\
uint32 count     # How many elements in the field\n\
";
  }

  static const char* value(const ::rtabmap_ros::GetMapResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetMapResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rtabmap_ros::GetMapResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rtabmap_ros::GetMapResponse_<ContainerAllocator>& v)
  {
    s << indent << "data: ";
    s << std::endl;
    Printer< ::rtabmap_ros::MapData_<ContainerAllocator> >::stream(s, indent + "  ", v.data);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RTABMAP_ROS_MESSAGE_GETMAPRESPONSE_H
