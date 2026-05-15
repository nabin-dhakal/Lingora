import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Dimensions } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import LessonpreviewModal from '../components/LessonpreviewModal';

const { width } = Dimensions.get('window');

const lessons = [
  { id: 1, title: 'Basics 1', description: 'Learn basic greetings', completed: true, locked: false },
  { id: 2, title: 'Basics 2', description: 'Numbers and colors', completed: true, locked: false },
  { id: 3, title: 'Phrases', description: 'Common phrases', completed: false, locked: false },
  { id: 4, title: 'Food', description: 'Food vocabulary', completed: false, locked: true },
  { id: 5, title: 'Animals', description: 'Animal names', completed: false, locked: true },
  { id: 6, title: 'Family', description: 'Family members', completed: false, locked: true },
  { id: 7, title: 'Clothing', description: 'Clothing items', completed: false, locked: true },
  { id: 8, title: 'Weather', description: 'Weather terms', completed: false, locked: true },
];

const getPosition = (index) => {
  const positions = [-80, 80, -60, 60, -90, 90, -50, 50];
  return positions[index % positions.length];
};

const HomeScreen = () => {
  const [modalVisible, setModalVisible] = useState(false);
  const [selectedLesson, setSelectedLesson] = useState(null);

  const handleLessonPress = (lesson) => {
    if (!lesson.locked) {
      setSelectedLesson(lesson);
      setModalVisible(true);
    }
  };

  const renderLessonNode = ({ item, index }) => {
    const bgColor = item.locked
      ? '#d9d9d9'
      : item.completed
      ? '#58CC02'
      : '#1CB0F6';

    let iconName = 'star';
    let iconColor = '#fff';
    if (item.locked) {
      iconName = 'lock-closed';
      iconColor = '#999';
    } else if (item.completed) {
      iconName = 'checkmark';
      iconColor = '#fff';
    }

    return (
      <View style={[styles.nodeWrapper, { marginLeft: width / 2 + getPosition(index) - 45 }]}>
        <TouchableOpacity
          activeOpacity={0.8}
          style={[styles.node, { backgroundColor: bgColor }]}
          onPress={() => handleLessonPress(item)}
        >
          <Ionicons name={iconName} size={34} color={iconColor} />
        </TouchableOpacity>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={styles.headerItem}>
          <Ionicons name="flame" size={22} color="#FF9600" />
          <Text style={styles.headerText}>14</Text>
        </View>
        <View style={styles.headerItem}>
          <Ionicons name="diamond" size={22} color="#1CB0F6" />
          <Text style={styles.headerText}>350</Text>
        </View>
        <View style={styles.headerItem}>
          <Ionicons name="heart" size={22} color="#FF4B4B" />
          <Text style={styles.headerText}>5</Text>
        </View>
      </View>

      <View style={styles.titleContainer}>
        <Text style={styles.title}>Sanskrit Basics</Text>
        <Text style={styles.subtitle}>Continue your learning journey</Text>
      </View>

      <FlatList
        data={lessons}
        keyExtractor={(item) => item.id.toString()}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={{ paddingVertical: 40, paddingBottom: 120 }}
        renderItem={renderLessonNode}
      />

      {selectedLesson && (
        <LessonpreviewModal
          visible={modalVisible}
          lesson={selectedLesson}
          onClose={() => setModalVisible(false)}
        />
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F7F7F7',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 18,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderColor: '#eee',
  },
  headerItem: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  headerText: {
    fontSize: 18,
    fontWeight: '700',
    color: '#444',
    marginLeft: 6,
  },
  titleContainer: {
    padding: 20,
  },
  title: {
    fontSize: 30,
    fontWeight: '800',
    color: '#333',
  },
  subtitle: {
    fontSize: 16,
    color: '#777',
    marginTop: 5,
  },
  nodeWrapper: {
    marginVertical: 18,
  },
  node: {
    width: 90,
    height: 90,
    borderRadius: 45,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.12,
    shadowRadius: 8,
    shadowOffset: { width: 0, height: 4 },
    elevation: 6,
  },
});

export default HomeScreen;