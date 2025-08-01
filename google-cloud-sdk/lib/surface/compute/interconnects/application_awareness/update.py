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
"""Command for enabling/disabling application awareness on interconnect and updating the profile description of the profile."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute.interconnects import client
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.compute.interconnects import flags

DETAILED_HELP = {
    'DESCRIPTION': """\
        *{command}* allows the user to enable or disable application awareness on Interconnect,
        as well as add/update the description of the application awareness on Interconnect profile.
        For an example, refer to the *EXAMPLES* section below.""",
    # pylint: disable=line-too-long
    'EXAMPLES': """\
        To update the application awareness config on
        Compute Engine interconnect in a project, run:

          $ {command} example-interconnect application-awareness update --enabled --profile-description="Some string"
        """,
    # pylint: enable=line-too-long
}


@base.UniverseCompatible
@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class UpdateConfig(base.DescribeCommand):
  """Updates application awareness configuration of a Compute Engine interconnect.

  *{command}* allows the user to enable or disable application awareness on
  Interconnect,as well as add/update the description of the application
  awareness on Interconnect profile..
  """

  INTERCONNECT_ARG = None

  @classmethod
  def Args(cls, parser):
    cls.INTERCONNECT_ARG = flags.InterconnectArgument()
    cls.INTERCONNECT_ARG.AddArgument(parser, operation_type='patch')
    flags.AddAaiEnabled(parser)
    flags.AddAaiProfileDescription(parser)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    ref = self.INTERCONNECT_ARG.ResolveAsResource(args, holder.resources)
    interconnect = client.Interconnect(ref, compute_client=holder.client)
    application_aware_interconnect = (
        interconnect.Describe().applicationAwareInterconnect
    )

    if args.enabled or args.profile_description:
      if (
          application_aware_interconnect is None
          or application_aware_interconnect
          == holder.client.messages.InterconnectApplicationAwareInterconnect()
      ):
        raise exceptions.BadArgumentException(
            '{}'.format('enabled' if args.enabled else 'profile-description'),
            "Interconnect '{}' does not have application awareness"
            ' config.'.format(ref.Name()),
        )

    if args.profile_description:
      application_aware_interconnect.profileDescription = (
          args.profile_description
      )

    return (
        interconnect.Patch(
            description=None,
            interconnect_type=None,
            requested_link_count=None,
            link_type=None,
            admin_enabled=None,
            noc_contact_email=None,
            location=None,
            labels=None,
            label_fingerprint=None,
            aai_enabled=args.enabled,
            application_aware_interconnect=application_aware_interconnect,
        ),
    )


UpdateConfig.detailed_help = DETAILED_HELP
