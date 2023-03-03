//odoo.define('amicales.OrgChartWidget', function (require) {
//    'use strict';
//
//    var Widget = require('web.Widget');
//    var rpc = require('web.rpc');
//
//    var OrgChartWidget = Widget.extend({
//      template: 'amicales.amicale',
//
//      init: function (parent, options) {
//        this._super.apply(this, arguments);
//        this.data = [];
//        this.selectedEmployee = null;
//      },
//
//      start: function () {
//        var self = this;
//
//        // Récupérer les données des employés depuis le serveur
//        rpc.query({
//          model: 'amicales.amicale',
//          method: 'search_read',
//          args: [[], ['name', 'nomAmicale']]
//        }).then(function (amicale) {
//          self.data =  amicale;
//          self.renderOrgChart();
//        });
//
//        return this._super.apply(this, arguments);
//      },
//
//      renderOrgChart: function () {
//        var self = this;
//        var rootNode = null;
//        var nodes = {};
//
//        // Créer les noeuds pour chaque employé
//        for (var i = 0; i < this.data.length; i++) {
//          var employee = this.data[i];
//          nodes[employee.id] = {
//            'id': amicale.id,
//            'name': amicale.nomAmicale,
//            'children': []
//          };
//          if (!nomAmicale.commision_ids) {
//            rootNode = nomAmicale.id;
//          }
//        }
//
//        // Ajouter les noeuds enfants aux noeuds parents
//        for (var nodeId in nodes) {
//          var  amicale = this.data.find(function (emp) { return emp.id === parseInt(nodeId); });
//          if (nomAmicale.commision_ids) {
//            nodes[nomAmicale.commision_ids[0]].children.push(nodes[nodeId]);
//          }
//        }
//
//        // Tracer l'organigramme
//        var orgChartContainer = document.getElementById('org_chart');
//        orgChartContainer.innerHTML = '';
//        if (rootNode) {
//          var rootNodeElement = this.createNodeElement(nodes[rootNode]);
//          orgChartContainer.appendChild(rootNodeElement);
//        }
//      },
//
//      createNodeElement: function (node) {
//        var self = this;
//        var nodeElement = document.createElement('div');
//        nodeElement.className = 'org-chart-node';
//        nodeElement.innerHTML = '<div class="org-chart-node-name">' + node.name + '</div>';
//
//        for (var i = 0; i < node.children.length; i++) {
//          var childNodeElement = this.createNodeElement(node.children[i]);
//          nodeElement.appendChild(childNodeElement);
//        }
//
//        nodeElement.addEventListener('click', function () {
//          self.selectedAmicale = self.data.find(function (emp) { return emp.id === node.id; });
//        });
//
//        return nodeElement;
//      },
//
//      addEmployee: function () {
//        var self = this;
//        var name = prompt("Nom de l'employé :");
//
//
//        if (name) {
//      var parentId = this.selectedEmployee ? this.selectedEmployee.id : false;
//      rpc.query({
//        model: 'amicales.amicale',
//        method: 'create',
//        args: [{
//          'nomAmicale: name,
//          'commision_ids': parentId
//        }]
//      }).then(function (result) {
//        self.reloadEmployees();
//      });
//    }
//  },
//
//  editEmployee: function () {
//    var self = this;
//    if (this.selectedEmployee) {
//      var name = prompt("Nom de l'employé :", this.selectedAmicale.name);
//      if (name) {
//        rpc.query({
//          model: 'mon_module.employee',
//          method: 'write',
//          args: [[this.selectedAmicale.id], {
//            'nomAmical': name
//          }]
//        }).then(function (result) {
//          self.reloadEmployees();
//        });
//      }
//    } else {
//      alert("Veuillez sélectionner un employé à modifier.");
//    }
//  },
//
//  deleteEmployee: function () {
//    var self = this;
//    if (this.selectedEmployee) {
//      rpc.query({
//        model: 'amicales.amical',
//        method: 'unlink',
//        args: [[this.selectedAmicale.id]]
//      }).then(function (result) {
//        self.reloadEmployees();
//      });
//    } else {
//      alert("Veuillez sélectionner un employé à supprimer.");
//    }
//  },
//
//  reloadEmployees: function () {
//    var self = this;
//    rpc.query({
//      model: 'amicales.amicale',
//      method: 'search_read',
//      args: [[], ['nomAmicale', 'commision_ids']]
//    }).then(function (amicale) {
//      self.data = amicale;
//      self.renderOrgChart();
//    });
//  }
//
//});
//
//return OrgChartWidget;
//});