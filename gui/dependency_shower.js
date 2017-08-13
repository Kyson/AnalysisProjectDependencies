/**
 * Created by kysonchao on 2017/8/12.
 */
'use strict'

$(document).ready(function () {
    var load_chat = function () {
        $.getJSON("output/module_dependencies_repr.json", function (module_dependencies_repr) {
            console.log(module_dependencies_repr);
            var nodes = [];
            var edges = [];
            for (var i = 0; i < module_dependencies_repr.length; i++) {
                var module_dependency_item = module_dependencies_repr[i];
                var module_name = module_dependency_item.name;
                var module_path = module_dependency_item.path;
                var module_dependencies = module_dependency_item.dependencies;
                nodes.push(
                    {data: {id: module_name, name: module_name}}
                );

                for (var j = 0; j < module_dependencies.length; j++) {
                    edges.push({
                        data: {
                            source: module_name,
                            target: module_dependencies[j]
                        }
                    })
                }
            }
            draw_chat(nodes, edges);
        });

        function draw_chat(nodes, edges) {
            var cy = cytoscape({
                container: $('#cy'),
                boxSelectionEnabled: false,
                autounselectify: false,
                selectionType: "additive",

                style: cytoscape.stylesheet()
                    .selector('node')
                    .css({
                        'content': 'data(name)',
                        'text-valign': 'center',
                        'color': 'white',
                        'background-opacity': 0.7,
                        'background-color': '#0099CC',
                        'text-outline-color': '#0099CC'
                    })
                    .selector('edge')
                    .css({
                        'curve-style': 'bezier',
                        'target-arrow-shape': 'triangle',
                        'target-arrow-color': '#CCCCCC',
                        'line-color': '#CCCCCC',
                        'width': 0.5
                    })
                    .selector(':selected')
                    .css({
                        'background-color': '#CCFF66',
                        'line-color': '#CCFF66',
                        'target-arrow-color': '#CCFF66',
                        'source-arrow-color': '#CCFF66'
                    })
                    .selector('.faded')
                    .css({
                        'opacity': 1.0,
                        'text-opacity': 0
                    }),
                elements: {
                    nodes: nodes,
                    edges: edges
                },
                layout: {
                    name: 'cose',
                    padding: 10
                }
            });

            function clearSelection() {
                var eles = cy.elements();
                for (var j = 0; j < eles.length; j++) {
                    eles[j].unselect();
                }
            }

            cy.on('tap', 'node', function (e) {
                clearSelection();
                var node = e.target;
                var neighborhood_dependencies = node.neighborhood("edge[source = \"" + node.data("id") + "\"]");
                console.log(neighborhood_dependencies);
                for (var i = 0; i < neighborhood_dependencies.length; i++) {
                    var neighborhood_node = cy.$("#" + neighborhood_dependencies[i].data("target"));
                    neighborhood_dependencies[i].select();
                    neighborhood_node.select();
                }
            });
            cy.on("tap", "edge", function (e) {
                clearSelection();
            })
        }
    };
    load_chat();
});

