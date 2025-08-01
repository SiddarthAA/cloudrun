# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
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

"""Stores lookup keys for help search table."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import cli_tree


ATTR = cli_tree.LOOKUP_ATTR
CAPSULE = cli_tree.LOOKUP_CAPSULE
CHOICES = cli_tree.LOOKUP_CHOICES
HIDDEN_CHOICES = cli_tree.LOOKUP_HIDDEN_CHOICES
COMMANDS = cli_tree.LOOKUP_COMMANDS
DEFAULT = cli_tree.LOOKUP_DEFAULT
DESCRIPTION = cli_tree.LOOKUP_DESCRIPTION
FLAGS = cli_tree.LOOKUP_FLAGS
IS_GLOBAL = cli_tree.LOOKUP_IS_GLOBAL
IS_HIDDEN = cli_tree.LOOKUP_IS_HIDDEN
NAME = cli_tree.LOOKUP_NAME
PATH = cli_tree.LOOKUP_PATH
POSITIONALS = cli_tree.LOOKUP_POSITIONALS
RELEASE = cli_tree.LOOKUP_RELEASE
SECTIONS = cli_tree.LOOKUP_SECTIONS

FLAG = 'flag'
COMMAND = 'command'
GENERATED = 'generated'
MARKDOWN = 'markdown'
POSITIONAL = 'positional'
SUBSECTIONS = 'subsections'
SUMMARY = 'summary'
TEXT = 'text'
RESULTS = 'results'
RELEVANCE = 'relevance'

DOT = '.'

# Part of command[RELEASE]
ALPHA = 'ALPHA'
BETA = 'BETA'
GA = 'GA'

# Part of command[PATH]
ALPHA_PATH = 'alpha'
BETA_PATH = 'beta'
