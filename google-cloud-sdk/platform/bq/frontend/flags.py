#!/usr/bin/env python
"""Flags shared across multiple commands."""

from typing import List, Optional

from absl import flags


def define_null_marker(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'null_marker',
      None,
      'An optional custom string that will represent a NULL value'
      'in CSV External table data.',
      flag_values=flag_values,
  )


def define_null_markers(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[List[str]]]:
  return flags.DEFINE_list(
      'null_markers',
      [],
      'An optional list of custom strings that will represent a NULL value'
      'in CSV External table data.',
      flag_values=flag_values,
  )


def define_time_zone(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'time_zone',
      None,
      'Default time zone that will apply when parsing timestamp values that'
      ' have no specific time zone. For example, "America/Los_Angeles".',
      flag_values=flag_values,
  )


def define_date_format(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'date_format',
      None,
      'Format elements that define how the DATE values are formatted in the'
      ' input files. For example, "MM/DD/YYYY".',
      flag_values=flag_values,
  )


def define_datetime_format(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'datetime_format',
      None,
      'Format elements that define how the DATETIME values are formatted in'
      ' the input files. For example, "MM/DD/YYYY HH24:MI:SS.FF3".',
      flag_values=flag_values,
  )


def define_time_format(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'time_format',
      None,
      'Format elements that define how the TIME values are formatted in the'
      ' input files. For example, "HH24:MI:SS.FF3".',
      flag_values=flag_values,
  )


def define_timestamp_format(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'timestamp_format',
      None,
      'Format elements that define how the TIMESTAMP values are formatted in'
      ' the input files. For example, "MM/DD/YYYY HH24:MI:SS.FF3".',
      flag_values=flag_values,
  )


def define_source_column_match(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_enum(
      'source_column_match',
      None,
      ['POSITION', 'NAME'],
      'Controls the strategy used to match loaded columns to the schema in CSV'
      ' External table data. Options include:'
      '\n POSITION: matches by position. This option assumes that the columns'
      ' are ordered the same way as the schema.'
      '\n NAME: matches by name. This option reads the header row as column'
      ' names and reorders columns to match the field names in the schema.',
      flag_values=flag_values,
  )


def define_parquet_map_target_type(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_enum(
      'parquet_map_target_type',
      None,
      ['ARRAY_OF_STRUCT'],
      'Specifies the parquet map type. If it is equal to ARRAY_OF_STRUCT,'
      ' then a map_field will be represented with a repeated struct (that has'
      ' key and value fields).',
      flag_values=flag_values,
  )


def define_reservation_id_for_a_job(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'reservation_id',
      None,
      'Reservation ID used when executing the job. Reservation should be in the'
      'format of project_id:reservation_id, project_id:location.reservation_id,'
      'or reservation_id',
      flag_values=flag_values,
  )


def define_event_driven_schedule(
    flag_values: flags.FlagValues,
) -> flags.FlagHolder[Optional[str]]:
  return flags.DEFINE_string(
      'event_driven_schedule',
      None,
      'Event driven schedule in json format. Example:'
      ' --event_driven_schedule=\'{"pubsub_subscription":'
      ' "projects/project-id/subscriptions/subscription-id"}\'. This flag'
      ' should not be used with --schedule, --no_auto_scheduling,'
      ' --schedule_start_time or --schedule_end_time.',
      flag_values=flag_values,
  )
