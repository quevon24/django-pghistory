# Generated by Django 4.2.6 on 2023-10-09 21:43

import pgtrigger.compiler
import pgtrigger.migrations
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0005_auto_20230408_1619"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="custommodel",
            name="int_field_updated",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="after_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            name="ignoreautofieldssnapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_int_field_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="custom_snapshot_update",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="custommodel",
            trigger=pgtrigger.compiler.Trigger(
                name="int_field_updated",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."integer_field" IS DISTINCT FROM (NEW."integer_field"))',
                    func='INSERT INTO "tests_custommodelevent" ("integer_field", "my_pk", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."integer_field", NEW."my_pk", _pgh_attach_context(), NOW(), \'int_field_updated\', NEW."my_pk"); RETURN NULL;',  # noqa
                    hash="f427ffcb88213b56059b9055bbde73d6e8e31569",
                    operation="UPDATE",
                    pgid="pgtrigger_int_field_updated_a1031",
                    table="tests_custommodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="after_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM (NEW."dt_field"))',
                    func='INSERT INTO "tests_eventmodelevent" ("dt_field", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'after_update\', NEW."id"); RETURN NULL;',  # noqa
                    hash="a34059f2a3f7cb3f34f672e1e1897049631e977b",
                    operation="UPDATE",
                    pgid="pgtrigger_after_update_5b8c8",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="ignoreautofieldssnapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="ignoreautofieldssnapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM (NEW."id") OR OLD."my_char_field" IS DISTINCT FROM (NEW."my_char_field") OR OLD."my_int_field" IS DISTINCT FROM (NEW."my_int_field"))',  # noqa
                    func='INSERT INTO "tests_ignoreautofieldssnapshotmodelevent" ("created_at", "id", "my_char_field", "my_int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "updated_at") VALUES (OLD."created_at", OLD."id", OLD."my_char_field", OLD."my_int_field", _pgh_attach_context(), NOW(), \'ignoreautofieldssnapshot\', OLD."id", OLD."updated_at"); RETURN NULL;',  # noqa
                    hash="9b76d83614f2de0a52eee7faaeb243008668c818",
                    operation="UPDATE",
                    pgid="pgtrigger_ignoreautofieldssnapshot_update_767f2",
                    table="tests_ignoreautofieldssnapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_int_field_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM (NEW."dt_field") OR OLD."int_field" IS DISTINCT FROM (NEW."int_field"))',  # noqa
                    func='INSERT INTO "tests_snapshotmodeldtfieldintfieldevent" ("dt_field", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."int_field", _pgh_attach_context(), NOW(), \'dt_field_int_field_snapshot\', NEW."id"); RETURN NULL;',  # noqa
                    hash="7a825bed05e4dce2aab1a4a51af23537de266da7",
                    operation="UPDATE",
                    pgid="pgtrigger_dt_field_int_field_snapshot_update_8246d",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM (NEW."dt_field"))',
                    func='INSERT INTO "tests_snapshotmodeldtfieldevent" ("dt_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", _pgh_attach_context(), NOW(), \'dt_field_snapshot\', NEW."id"); RETURN NULL;',  # noqa
                    hash="d4200e362d70ee8a3d90968b7d66f1faeee08e18",
                    operation="UPDATE",
                    pgid="pgtrigger_dt_field_snapshot_update_22f55",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="custom_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM (NEW."id") OR OLD."int_field" IS DISTINCT FROM (NEW."int_field") OR OLD."fk_field_id" IS DISTINCT FROM (NEW."fk_field_id"))',  # noqa
                    func='INSERT INTO "tests_customsnapshotmodel" ("fk_field_id", "id", "int_field", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."fk_field_id", NEW."id", NEW."int_field", NOW(), \'custom_snapshot\', NEW."id"); RETURN NULL;',  # noqa
                    hash="88d880fe4785b823fd0bcc32a85a58c8deb389b6",
                    operation="UPDATE",
                    pgid="pgtrigger_custom_snapshot_update_5af3e",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
    ]
