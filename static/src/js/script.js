 addRecord: function () {
  var self = this;
  var model = 'amicales.membre';

  // Ouvrir le formulaire de création dans un dialogue modal
  this.do_action({
    name: "Créer un nouvel employé",
    type: "ir.actions.act_window",
    res_model: model,
    views: [[false, "form"]],
    target: "new",
    flags: {form: {'action_buttons': true}}
  }).then(function () {
    // Rafraîchir la vue tree après avoir créé le record
    return self.reload();
  });
}
