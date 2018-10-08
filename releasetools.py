# Copyright (C) 2019 The Unlegacy Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common

def SystemResize(info):
  if not SystemResize.ran_once:
    e2fsck = '"/sbin/e2fsck", "-fy"'; run_prog = 'run_program('
    _, sys_dev = common.GetTypeAndDevice("/system", info.info_dict)
    sys_dev = ', "' + sys_dev + '");'
    try:
      resize2fs = '"/tmp/' + \
        info.input_zip.getinfo("install/bin/resize2fs_static").filename + '"'
    except:
      resize2fs = '"/sbin/resize2fs"'
    info.script.AppendExtra(run_prog + e2fsck + sys_dev)
    info.script.AppendExtra(run_prog + resize2fs + sys_dev)
    info.script.AppendExtra(run_prog + e2fsck + sys_dev)
    SystemResize.ran_once = True

SystemResize.ran_once = False

def FullOTA_PostValidate(info):
  SystemResize(info)

def FullOTA_InstallEnd(info):
  SystemResize(info)
