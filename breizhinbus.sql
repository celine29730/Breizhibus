-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 30, 2020 at 12:59 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breizhinbus`
--

-- --------------------------------------------------------

--
-- Table structure for table `arret`
--

CREATE TABLE `arret` (
  `id_arret` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arret`
--

INSERT INTO `arret` (`id_arret`, `nom`, `adresse`) VALUES
(1, 'Korrigan', '1 impasse du Korrigan'),
(2, 'Morgana', '2 place de Morgana'),
(4, 'L\'ankou', '3 Place de L\'Ankou'),
(5, 'Ys', '4 rue de l\'Ys'),
(6, 'Viviane', '5 Avenue de Viviane'),
(7, 'Guénolé', '6 Rue de Saint Guénolé');

-- --------------------------------------------------------

--
-- Table structure for table `arret_ligne`
--

CREATE TABLE `arret_ligne` (
  `id_lignes` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL,
  `ligne` varchar(100) NOT NULL,
  `arret` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arret_ligne`
--

INSERT INTO `arret_ligne` (`id_lignes`, `id_arret`, `ligne`, `arret`) VALUES
(8, 1, 'Rouge', 'Korrigan'),
(10, 1, 'Bleu', 'Korrigan'),
(11, 1, 'Noire', 'Korrigan'),
(8, 2, 'Rouge', 'Morgana'),
(9, 2, 'Vert', 'Morgana'),
(8, 4, 'Rouge', 'L\'Ankou'),
(11, 4, 'Noire', 'L\'Ankou'),
(9, 5, 'Vert', 'Ys'),
(10, 5, 'Bleu', 'Ys'),
(10, 6, 'Bleu', 'Viviane'),
(11, 6, 'Noire', 'Viviane'),
(9, 7, 'Vert', 'Guénolé'),
(10, 7, 'Bleu', 'Guénolé');

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numero` varchar(4) NOT NULL,
  `immatriculation` varchar(7) NOT NULL,
  `nombre_place` int(11) NOT NULL,
  `id_lignes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_place`, `id_lignes`) VALUES
(1, 'BB01', 'CA123DO', 20, 8),
(2, 'BB02', 'NO123EL', 30, 9),
(3, 'BB03', 'JE123UX', 20, 10),
(4, 'BB04', 'RE123PA', 30, 8),
(5, 'BB05', 'PU123LL', 0, 11),
(6, 'BB06', 'FE123TE', 0, 11),
(7, 'BB07', 'GFDF', 7, 11),
(8, 'BB07', 'DRRR', 6, 11),
(19, 'BB10', 'EZ123EQ', 7, 9),
(20, 'BB12', 'RE123AQ', 7, 9),
(21, 'BB13', 'RT123RE', 8, 9),
(22, 'BB14', 'RE123YT', 8, 10),
(23, 'BB16', 'TR123EZ', 8, 10),
(24, 'BB23', 'EZ123TR', 7, 9);

-- --------------------------------------------------------

--
-- Table structure for table `lignes`
--

CREATE TABLE `lignes` (
  `id_lignes` int(11) NOT NULL,
  `nom_ligne` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lignes`
--

INSERT INTO `lignes` (`id_lignes`, `nom_ligne`) VALUES
(8, 'Rouge'),
(9, 'Vert'),
(10, 'Bleu'),
(11, 'Noire');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arret`
--
ALTER TABLE `arret`
  ADD PRIMARY KEY (`id_arret`);

--
-- Indexes for table `arret_ligne`
--
ALTER TABLE `arret_ligne`
  ADD KEY `id_lignes` (`id_lignes`),
  ADD KEY `id_arret` (`id_arret`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `id_lignes` (`id_lignes`);

--
-- Indexes for table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`id_lignes`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arret`
--
ALTER TABLE `arret`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `id_lignes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arret_ligne`
--
ALTER TABLE `arret_ligne`
  ADD CONSTRAINT `arret_ligne_ibfk_1` FOREIGN KEY (`id_lignes`) REFERENCES `lignes` (`id_lignes`),
  ADD CONSTRAINT `arret_ligne_ibfk_2` FOREIGN KEY (`id_arret`) REFERENCES `arret` (`id_arret`);

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_lignes`) REFERENCES `lignes` (`id_lignes`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
