<?php

// Función para dibujar el grafo
function drawGraph($nodes, $edges)
{
    echo '<svg width="800" height="600">';
    
    // Dibujar aristas
    foreach ($edges as $edge) {
        echo '<line x1="' . $nodes[$edge[0]]['x'] . '" y1="' . $nodes[$edge[0]]['y'] . '" x2="' . $nodes[$edge[1]]['x'] . '" y2="' . $nodes[$edge[1]]['y'] . '" stroke="gray" />';
    }

    // Dibujar nodos después de las aristas para que estén encima
    foreach ($nodes as $node) {
        echo '<circle cx="' . $node['x'] . '" cy="' . $node['y'] . '" r="20" fill="skyblue" stroke="black" />';
        echo '<text x="' . ($node['x'] - 15) . '" y="' . ($node['y'] + 5) . '" fill="black">' . $node['label'] . '</text>';
    }

    echo '</svg>';
}

// Definir nodos y aristas
$nodes = [
    ["label" => "Educación a Distancia (EaD)", "x" => 100, "y" => 100],
    ["label" => "Historia y Evolución", "x" => 200, "y" => 50],
    ["label" => "Tecnología y Herramientas", "x" => 300, "y" => 100],
    ["label" => "Rol del Docente", "x" => 200, "y" => 150],
    ["label" => "Aprendizaje Autónomo", "x" => 100, "y" => 200],
    ["label" => "Paradigma Educativo", "x" => 300, "y" => 200],
    ["label" => "Sociedad Digital", "x" => 200, "y" => 250],
    ["label" => "Desafíos y Perspectivas", "x" => 100, "y" => 300],
];

$edges = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [1, 2],
    [1, 5],
    [2, 3],
    [3, 6],
    [4, 3],
    [5, 4],
    [6, 7],
];

// Dibujar el grafo
drawGraph($nodes, $edges);

?>
