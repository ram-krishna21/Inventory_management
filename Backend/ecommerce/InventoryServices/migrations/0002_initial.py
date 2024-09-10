# Generated by Django 4.1.7 on 2024-09-10 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("InventoryServices", "0001_initial"),
        ("OrderServices", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ProductServices", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="warehouse",
            name="Warehouse_manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="warehouse_manager_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="warehouse",
            name="added_by_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_by_user_id_warehouse",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="warehouse",
            name="domain_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="domain_user_id_warehouse",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="rackandshelvesandfloor",
            name="added_by_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_by_user_id_rack_shelf_floor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="rackandshelvesandfloor",
            name="domain_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="domain_user_id_products_rack_shelf_floor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="rackandshelvesandfloor",
            name="warehouse_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rack_shelves_floors",
                to="InventoryServices.warehouse",
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="added_by_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_by_user_id_inventory_log",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="domain_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="domain_user_id_inventory_log",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="inventory_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inventory_id_inventory_log",
                to="InventoryServices.inventory",
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="po_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="po_id_inventory_log",
                to="OrderServices.purchaseorder",
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="rack_shelf_floor_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rack_shelf_floor_id_inventory_log",
                to="InventoryServices.rackandshelvesandfloor",
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="so_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="so_id_inventory_log",
                to="OrderServices.salesorder",
            ),
        ),
        migrations.AddField(
            model_name="inventorylog",
            name="warehouse_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="warehouse_id_inventory_log",
                to="InventoryServices.warehouse",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="added_by_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_by_user_id_inventory",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="domain_user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="domain_user_id_inventory",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="product_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_id",
                to="ProductServices.products",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="purchase_order_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_order_id",
                to="OrderServices.purchaseorder",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="purchase_order_item_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_order_item_id",
                to="OrderServices.purchaseorderitems",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="purchase_order_item_inwarded_item_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_order_item_id",
                to="OrderServices.purchaseorderiteminwardedlog",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="rack_shelf_floor_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rack_shelf_floor_id",
                to="InventoryServices.rackandshelvesandfloor",
            ),
        ),
        migrations.AddField(
            model_name="inventory",
            name="warehouse_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="warhouse_id",
                to="InventoryServices.warehouse",
            ),
        ),
    ]
