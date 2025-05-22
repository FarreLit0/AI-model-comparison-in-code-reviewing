function comparator(a, b) {
  var aLastAccessTime = a.get("lastAccessTime");
  var bLastAccessTime = b.get("lastAccessTime");
  if (aLastAccessTime !== bLastAccessTime) {
    return bLastAccessTime - aLastAccessTime;
  } else if (aLastAccessTime && !bLastAccessTime) {
    return -1;
  } else if (!aLastAccessTime && bLastAccessTime) {
    return 1;
  }
  return 0;
}