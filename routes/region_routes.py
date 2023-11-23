from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from dbase import db
from models import Region
from forms import RegionForm, RegionListForm, RegionDeleteForm, RegionUpdateForm

region_bp = Blueprint('region_bp', __name__)


@region_bp.route('/web/region/add', methods=['GET', 'POST'])
def add_region_web():
    form = RegionForm()

    if form.validate_on_submit():
        name = form.name.data
        number = form.number.data

        region = Region(name=name, id=number)
        db.session.add(region)
        db.session.commit()

        return render_template('region-add.html', form=form, result='Region added successfully')

    return render_template('region-add.html', form=form, result=None)


@region_bp.route('/web/region/update', methods=['GET', 'POST'])
def update_region_web():
    form = RegionUpdateForm()

    if form.validate_on_submit():
        id = form.id.data
        new_id = form.new_id.data

        region = Region.query.get(id)
        if not region:
            flash('Region not found', 'danger')
        else:
            region.id = new_id
            db.session.commit()
            flash('Region updated successfully', 'success')
            return redirect(url_for('region_bp.update_region_web'))

    return render_template('region-update.html', form=form)


@region_bp.route('/web/region/delete', methods=['GET', 'POST'])
def delete_region_web():
    form = RegionDeleteForm()

    if form.validate_on_submit():
        id = form.id.data

        region = Region.query.get(id)
        if not region:
            flash('Region not found', 'danger')
        else:
            db.session.delete(region)
            db.session.commit()
            flash('Region deleted successfully', 'success')
            return redirect(url_for('region_bp.delete_region_web'))

    return render_template('region-delete.html', form=form)


@region_bp.route('/web/region', methods=['GET'])
def get_region_web():
    form = RegionListForm()
    regions = Region.query.all()
    return render_template('region-list.html', regions=regions, form=form)
