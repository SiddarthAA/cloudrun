# -*- coding: utf-8 -*- #
# Copyright 2025 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The gcloud.run.compose group."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
@base.DefaultUniverseOnly
class Compose(base.Group):
  """Support Docker Compose workflows on Cloud Run.

  This command group provides tools for Docker Compose developers to
  deploy services to Cloud Run using `compose.yaml` as the input source.
  """

  detailed_help = {
      'EXAMPLES': """\
          To bring up a Docker Compose service on Cloud Run, run:

            $ {command} up compose.yaml
      """,
  }
