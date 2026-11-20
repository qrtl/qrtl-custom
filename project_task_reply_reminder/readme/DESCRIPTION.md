This module schedules a "Reply to Customer" activity on a task when a
customer's public message has had no public reply from an internal user
within a set number of working hours.

The clock starts when a customer message moves the task to the customer
reply stage (see `project_task_reply_stage`). Further customer messages
do not restart it. A public message from an internal user, or moving the
task out of the reply stage, stops the clock and marks any open reminder
as done. Internal notes do not count as a reply.

The activity goes to the task's first assignee, or to the project
manager when the task has no assignee.
