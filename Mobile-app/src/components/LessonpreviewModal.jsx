import { Modal, View, Text, StyleSheet, TouchableOpacity } from "react-native";

const LessonpreviewModal = ({ visible, onClose, lesson }) => {
  return (
    <Modal visible={visible} animationType="slide" transparent onRequestClose={onClose}>
      <View style={styles.modalContainer}>
        <View style={styles.card}>
          <Text style={styles.lessonTitle}>{lesson?.title}</Text>
          <Text style={styles.lessonDescription}>{lesson?.description}</Text>
          <TouchableOpacity style={styles.startButton} onPress={onClose}>
            <Text style={styles.startButtonText}>Start Lesson</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={onClose}>
            <Text style={styles.closeText}>Close</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

const styles = StyleSheet.create({
  modalContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0, 0, 0, 0.5)",
  },
  card: {
    backgroundColor: "#fff",
    borderRadius: 16,
    padding: 30,
    width: "85%",
    alignItems: "center",
  },
  lessonTitle: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 10,
    color: "#333",
  },
  lessonDescription: {
    fontSize: 16,
    color: "#666",
    marginBottom: 30,
    textAlign: "center",
  },
  startButton: {
    backgroundColor: "#58CC02",
    paddingVertical: 14,
    paddingHorizontal: 50,
    borderRadius: 12,
    marginBottom: 12,
    width: "100%",
    alignItems: "center",
  },
  startButtonText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
  },
  closeText: {
    color: "#999",
    fontSize: 14,
    marginTop: 4,
  },
});

export default LessonpreviewModal;